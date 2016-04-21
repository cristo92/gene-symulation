import math
import numpy as np

from BaseModel import BaseModel

class BVTH2(BaseModel):
	def run(self, samples):
		k0 = self.k0
		alpha = self.alpha
		beta = self.beta
		gamma = self.gamma

		delta = alpha * alpha + 4 * alpha * k0 * beta / gamma
		A0 = (- alpha + math.sqrt(delta)) * gamma / (2 * k0 * beta)
		A1 = 1 - A0
		n0 = k0 * A0 * A0 / gamma
		n1 = (gamma * n0 + beta * n0 * n0 / A0 - k0 * A0) / alpha
		n = n0 + n1

		return {
			"n": n,
			"A0": A0,
			"A1": A1,
			"n_var": 0
		}