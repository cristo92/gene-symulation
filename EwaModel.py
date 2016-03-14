import math

from BaseModel import BaseModel

class EwaModel(BaseModel):
	def run(self, samples):
		k0 = self.k0
		k1 = self.k1
		alpha = self.alpha
		beta = self.beta
		gamma = self.gamma
		tau = self.tau

		delta = (k0 * alpha * tau + 2 * k0 + (alpha * gamma) / beta + 2 * (alpha *k0) / gamma - alpha + alpha * alpha / beta)
		delta *= delta
		delta += 4 * (- k0 * alpha * tau - k0 - alpha * gamma / beta - alpha * k0 / gamma + alpha) * (k0 + alpha * k0 / gamma)

		A1_1 = k0 * alpha * tau + 2 * k0 + alpha * gamma / beta + 2 * alpha * k0 / gamma - alpha + alpha * alpha / beta
		A1_2 = A1_1 + math.sqrt(delta)
		A1_1 -= math.sqrt(delta)
		t = 2 * (k0 * alpha * tau + k0 + alpha * gamma / beta + alpha * k0 / gamma - alpha)
		A1_1 /= t
		A1_2 /= t

		A1 = 0.0
		if A1_1 >= 0 and A1_1 <= 1:
			A1 = A1_1
		else:
			A1 = A1_2

		#print "{0} {1} {2}".format(A1_1, A1_2, A1)

		n = k0 / gamma + (1 - k0 / gamma) * A1
		return {
			"A0": 1 - A1,
			"A1": A1,
			"n": n
			}