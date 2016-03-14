import math
import numpy as np

from BaseModel import BaseModel

class MyModel(BaseModel):
	def run(self, samples):
		k0 = self.k0
		k1 = self.k1
		alpha = self.alpha
		beta = self.beta
		gamma = self.gamma
		tau = self.tau

		a = k0 - k0 * np.exp(-alpha * tau)
		b = -k0 + k0 * np.exp(-alpha * tau) - k0 + k0 * np.exp(-alpha * tau) -k0 - alpha * gamma / beta - k0 * alpha / gamma +\
		 alpha * alpha / beta - alpha * alpha / beta
		c = k0 - k0 * np.exp(-alpha * tau) + k0 + alpha * gamma / beta + k0 * alpha / gamma + alpha * alpha / beta + k0 +\
		 alpha * k0 / gamma + alpha
		d = -k0 - alpha * k0 / gamma - alpha
		T = np.roots([a,b,c,d])


		A1 = 0.0
		for t in T:
			if t >= 0.0 and t <= 1.0:
				A1 = t

		n = k0 / gamma + (1 - k0 / gamma) * A1

		return {
			"A0": 1 - A1,
			"A1": A1,
			"n": n
			}