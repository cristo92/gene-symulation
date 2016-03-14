import math
import numpy as np

from BaseModel import BaseModel

class PNAS(BaseModel):
	def run(self, samples):
		A = self.k0
		k_1 = self.alpha
		k1 = self.beta
		B = self.gamma

		epsilon = k1 / k_1

		n = n1 = n2 = A / (B + epsilon * A)

		return {
			"n": n,
			"A0": 0,
			"A1": 0
		}