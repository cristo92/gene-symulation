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
		delta = np.sqrt(beta * gamma * beta * gamma - 4 * k0 * alpha * beta)
		x1 = (delta - beta * gamma) / alpha

		return (x1, 0)