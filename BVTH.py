import math
import numpy as np

from BaseModel import BaseModel

class PNAS(BaseModel):
	def run(self, samples):
		n = self.k0 / (self.gamma + self.beta * self.k0 / self.alpha)
		A0 = self.alpha / (self.alpha + self.beta * n)

		return {
			"n": n,
			"A0": A0,
			"A1": 1 - A0
		}