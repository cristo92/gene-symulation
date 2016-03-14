import numpy as np
from numpy.random import exponential, random_sample

def weighted_values(values, probabilities, size=1):
	s = sum(probabilities)
	probabilities = map(lambda x: x/s, probabilities)
	bins = np.add.accumulate(probabilities)
	return values[np.digitize(random_sample(size), bins)]

class State:
	def __init__(self, n=0, dna=0, t=0):
		self.n = n
		self.dna = dna
		self.t = t

	def __str__(self):
		return "{0} {1} {2}".format(self.n, self.dna, self.t)