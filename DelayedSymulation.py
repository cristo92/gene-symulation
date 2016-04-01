from BaseModel import BaseModel
from utils import weighted_values, State
import math
import numpy as np
from numpy.random import exponential
from sys import stdout

class DelayedSymulation(BaseModel):
	def run(self, samples):
		initial_state = State(self.n_beg, self.dna_beg)
		mean_values = []
		history = []
		A = [ [], [] ]
		N = []
		init_samples = samples

		stdout.write("Symulation progress...\nAlpha({}) Beta({}) k({}) gamma({}) tau({})\n0%".format(self.alpha, self.beta, self.k0, self.gamma, self.tau))
		stdout.flush()

		while samples > 0:
			samples = samples - 1
			time = 0.0
			mean = 0.0
			counter = 0
			last_dna_change = self.t_const
			last_n_change = self.t_const
			_A = [0, 0]
			_N = 0

			state = initial_state
			eggs = []
			while time < self.t_max:
				lam = 0.0
				if state.dna == 0:
					lam += self.k0
					lam += state.n * self.beta
				elif state.dna == 1:
					lam += self.k1
					lam += self.alpha
				lam += state.n * self.gamma

				time += exponential(1. / lam)
				values = []
				probabilities = []
				if state.dna == 0:
					values = ["k", "beta","gamma"]
					probabilities = [self.k0, state.n * self.beta, state.n * self.gamma]
				elif state.dna == 1:
					values = ["k", "alpha", "gamma"]
					probabilities = [self.k1, self.alpha, state.n * self.gamma]
				event = weighted_values(values, probabilities)
				
				if event == "k":
					eggs.append(time)
				elif event == "beta":
					if time > self.t_const:
						_A[state.dna] += (time - last_dna_change)
						last_dna_change = time
					state.dna = 1
				elif event == "alpha":
					if time > self.t_const:
						_A[state.dna] += (time - last_dna_change)
						last_dna_change = time
					state.dna = 0
				elif event == "gamma":
					if time > self.t_const:
						_N += (time - last_n_change) * state.n
						last_n_change = time
					state.n -= 1
				while eggs and eggs[0] + self.tau <= time:
					if time > self.t_const:
						_N += (time - last_n_change) * state.n
						last_n_change = time
					state.n += 1
					eggs = eggs[1:]
			
			_A[state.dna] += (time - last_dna_change)
			_N += (time - last_n_change) * state.n

			A[0].append(_A[0] / (self.t_max - self.t_const))
			A[1].append(_A[1] / (self.t_max - self.t_const))
			N.append(_N / (self.t_max - self.t_const))

			stdout.write("\r%d%%" % int((init_samples - samples) * 100 / init_samples))
			stdout.flush()

		stdout.write("\n") # move the cursor to the next line

		for n in N:
			print n
		print np.var(N)

		A0 = np.mean(A[0])
		A1 = np.mean(A[1])

		return {
			"A0": A0,
			"A1": A1,
			"n": np.mean(N),
			'n_var': np.var(N)
		}
