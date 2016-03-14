from BaseModel import BaseModel
from utils import weighted_values, State
from numpy.random import exponential
import numpy as np

class NoneDelay(BaseModel):
	def run(self, samples):
		initial_state = State(self.n_beg, self.dna_beg, 0)
		mean_values = []
		history = []

		while samples > 0:
			samples = samples - 1
			time = 0.0
			mean = 0.0
			counter = 0.0
			history.append(initial_state)
			while time < self.t_max:
				state = history[-1]
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
					new_state = State(state.n + 1, state.dna, time)
				elif event == "beta":
					new_state = State(state.n, 1, time)
				elif event == "alpha":
					new_state = State(state.n, 0, time)
				elif event == "gamma":
					new_state = State(state.n - 1, state.dna, time)
				history.append(new_state)
			
			mean_values.append(mean / counter)
			history = []
		#print mean_values
		#print "\n"

		return (np.mean(mean_values), np.var(mean_values))



