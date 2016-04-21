import math
import numpy as np

from BaseModel import BaseModel

class MyPNAS(BaseModel):
	def run(self, samples):
		k0 = self.k0
		alpha = self.alpha
		beta = self.beta
		gamma = self.gamma

		#print beta * gamma - 4 * k0 * alpha * beta
		k0_delta = np.sqrt(alpha * gamma * alpha * gamma + 4 * k0 * alpha * beta * gamma)
		n = (k0_delta - alpha * gamma) / (2 * beta * gamma)

		A0 = gamma * n / k0
		A1 = 1 - A0
		print A0, A1, n

		return {
			"n": n,
			"A0": A0,
			"A1": A1,
			"n_var": 0
		}