from BaseModel import BaseModel
import math

class MiekiszSzymanska(BaseModel):
	def run(self, samples):
		x_eq = self.alpha / self.beta
		x_ad = (self.k0 + self.k1) / (2 * self.gamma)
		omega = self.alpha / self.gamma

		a = omega - 2 * x_ad * (omega + 1) - x_eq
		b = (4 * x_ad + x_eq - 1) * omega + 4 * x_ad + x_eq
		c = - 2 * x_ad * (omega + 1)

		delta = math.sqrt(b * b - 4 * a * c)
		A1_1 = (0 - delta - b) / (2 * a)
		A1_2 = (delta - b) / (2 * a)

		A1 = 0
		if A1_1 > 0 and A1_1 < 1:
			A1 = A1_1
		elif A1_2 > 0 and A1_2 < 1:
			A1 = A1_2

		A0 = 1 - A1
		n = (self.k0 / self.gamma) * A0 + (self.k1 / self.gamma) * A1 + A1

		return {
			"A0": A0,
			"A1": A1,
			"n": n
		}