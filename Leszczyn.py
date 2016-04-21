import math
import numpy as np

from BaseModel import BaseModel

class MyModel(BaseModel):
	""" Wersja bez A0 w 2.14 i 2.15 """
	def run(self, samples):
		k0 = self.k0
		k1 = self.k1
		alpha = self.alpha
		beta = self.beta
		gamma = self.gamma
		tau = self.tau

		#a = k0 * (1 - np.exp(-alpha * tau)) + gamma * alpha / beta - alpha * alpha / beta - alpha * (1 - k0 / gamma) + alpha * alpha / beta
		#b = 0 - k0 - k0 * (1 - np.exp(-alpha * tau)) - gamma * alpha / beta + alpha *(1 - k0 / gamma) - alpha * alpha / beta - alpha * k0 / gamma
		#c = k0 + alpha * k0 / gamma
		a = 2 * k0 - k0 * np.exp(- alpha * tau) - alpha + gamma * alpha / beta + alpha * k0 / gamma
		b = - 3 * k0 + k0 * np.exp(- alpha * tau) - gamma * alpha / beta - 2 * alpha * k0 / gamma + alpha - alpha * alpha / beta
		c = k0 + alpha * k0 / gamma

		delta = math.sqrt(b * b - 4 * a * c)
		A1_1 = (- delta - b ) / (2 * a)
		A1_2 = (delta - b) / (2 * a)

		A1 = 0
		if A1_1 > 0 and A1_1 < 1:
			A1 = A1_1
		elif A1_2 > 0 and A1_2 < 1:
			A1 = A1_2
		A0 = 1 - A1

		n = A1 + k0 * A0 / gamma

		return {
			"A0": A0,
			"A1": A1,
			"n": n
			}