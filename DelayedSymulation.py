from BaseModel import BaseModel
from utils import weighted_values, State
import math
import numpy as np
from numpy.random import exponential

class DelayedSymulation(BaseModel):
	def run(self, samples):
		initial_state = State(self.n_beg, self.dna_beg)
		mean_values = []
		pr_values = []
		history = []

		while samples > 0:
			samples = samples - 1
			time = 0.0
			mean = 0.0
			counter = 0.0
			pr1 = 0.0
			last_dna_change = 0

			state = initial_state
			eggs = []
			while time < self.t_max:
	#			print "{0} {1} {2:.2f} {3}".format(state.n, state.dna, time, eggs)
				lam = 0.0
				if state.dna == 0:
					lam += self.k0
					lam += state.n * self.beta
				elif state.dna == 1:
					lam += self.k1
					lam += self.alpha
				lam += state.n * self.gamma
				if time > self.t_const:
					mean += state.n
					counter += 1
					pr1 += state.dna

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
					state.dna = 1
				elif event == "alpha":
					state.dna = 0
				elif event == "gamma":
					state.n -= 1
				while eggs and eggs[0] + self.tau <= time:
					state.n += 1
					eggs = eggs[1:]
			
			mean_values.append(mean / counter)
			pr_values.append(pr1 / counter)
		#print mean_values
		#print "\n"
		#print "{0} {1}\n".format(np.mean(mean_values), np.var(mean_values))
		#print "{0} {1}\n".format(np.mean(pr_values), np.var(pr_values))

		return (np.mean(mean_values), np.var(mean_values))
