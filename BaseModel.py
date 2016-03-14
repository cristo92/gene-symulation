import sys

class BaseModel(object):
	def __init__(self, conf):
		self.conf = conf

	def read_data(self):
		f = open(sys.argv[1], "r")
		for line in f:
			line = line.split('=')
			line = map(lambda x: x.strip(), line)
			if line[0] == 'alpha':
				self.alpha = float(line[1])
			elif line[0] == 'beta':
				self.beta = float(line[1])
			elif line[0] == 'k0':
				self.k0 = float(line[1])
			elif line[0] == 'k1':
				self.k1 = float(line[1])
			elif line[0] == 'gamma':
				self.gamma = float(line[1])
			elif line[0] == 'tau':
				self.tau = float(line[1])
			elif line[0] == 't_max':
				self.t_max = float(line[1])
			elif line[0] == 't_const':
				self.t_const = float(line[1])
			elif line[0] == 'n_beg':
				self.n_beg = float(line[1])
			elif line[0] == 'dna_beg':
				self.dna_beg = float(line[1])

	def run(self, samples):
		return {
			"A0": -1,
			"A1": -1,
			"n": -1
		}