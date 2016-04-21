import sys
import argparse

ALL = ["PNAS", "DelayedSymulation", "EwaModel", "MyModel", "MiekiszSzymanska"]

def print_output(args, name, tex_name, A0, n, T):
	if not args.tex:
		print("============ A0 ============")
		print("{}\t\t{}".format(name, "\t".join([str(t) for t in T])))
		for model in args.models:
			_A0 = A0[model]
			print("{}{}{}".format(model[:15], "\t" * max(1, 2 - len(model)/8), 
			           "\t".join(["{:.3f}".format(t) for t in _A0])))
		print("============ n =============")
		print("{}\t\t{}".format(name, "\t".join([str(t) for t in T])))
		for model in args.models:
			_n = n[model]
			print("{}{}{}".format(model[:15], "\t" * max(1, 2 - len(model)/8), 
			           "\t".join(["{:.3f}".format(t) for t in _n])))
	else:
		print("============ A0 ============")
		print("{} &\t\t{}\\\\".format(tex_name, "&\t".join([str(t) for t in T])))
		for model in args.models:
			_A0 = A0[model]
			print("{}{}{}\\\\".format(model[:15], "\t" * max(1, 2 - len(model)/8), 
			           "\t".join(["&{:.3f}".format(t) for t in _A0])))
		print("============ n =============")
		print("{} &\t\t{}\\\\".format(tex_name, "&\t".join([str(t) for t in T])))
		for model in args.models:
			_n = n[model]
			print("{}{}{}\\\\".format(model[:15], "\t" * max(1, 2 - len(model)/8), 
			           "\t".join(["&{:.3f}".format(t) for t in _n])))

if __name__ == "__main__":
	T = [0, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1, 2.5, 5]
	O = [0.5, 1, 2, 5, 10, 20, 50, 100]
	P = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]

	parser = argparse.ArgumentParser(description="Stochastic simulation")
	parser.add_argument("config", help="Config file")
	parser.add_argument("-s", "--samples", type=int, help="Number of times simulation is ran. Result is mean value of all times.")
	parser.add_argument("models", help="Models which we're going to use.", nargs="+")
	parser.add_argument("-T", "--tau", action="store_true", help="If yes print table depends of Tau: {}".format(str(T)))
	parser.add_argument("-O", "--omega", action="store_true", help="If yes print table depends of Omega (alpha/gamma): {}".format(str(O)))
	parser.add_argument("-S", "--simple", action="store_true", help="If yes print output of config file.")
	parser.add_argument("-P", "--pnas", action="store_true", help="If yes print table depends of Omega (beta/alpha): {}".format(str(P)))
	parser.add_argument("-t", "--tex", action="store_true", help="Prints output in latex-friendly version.")

	args = parser.parse_args()

	conf = args.config
	samples = vars(args).get('samples', 1)
	

	if "all" in args.models:
		args.models = ALL

	if args.simple:
		for model in args.models:
			Model = getattr(__import__(model), model)
			m = Model(conf)
			m.read_data()

			ret = m.run(samples)
			print("{}\t{}\t{}\t{}".format(model, ret['A0'], ret['n'], ret.get('n_var', 0)))

	if args.tau:
		A0 = {}
		n = {}
		for model in args.models:
			Model = getattr(__import__(model), model)
			m = Model(conf)
			m.read_data()

			_A0 = []
			_n = []
			for tau in T:
				m.tau = tau
				ret = m.run(samples)
				_A0.append(ret['A0'])
				_n.append(ret['n'])
			A0[model] = _A0
			n[model] = _n

		print_output(args, "Tau", "\\tau", A0, n, T)
		

	if args.omega:
		A0 = {}
		n = {}
		n_var = {}

		# alpha = O * gamma
		# k0 = 80 * gamma
		# beta = alpha / 100
		for model in args.models:
			Model = getattr(__import__(model), model)
			m = Model(conf)
			m.read_data()

			_A0 = []
			_n = []
			_n_var = []
			for omega in O:
				m.alpha = omega * m.gamma
				m.k0 = 80 * m.gamma
				m.beta = m.alpha / 100
				ret = m.run(samples)
				_A0.append(ret['A0'])
				_n.append(ret['n'])
				_n_var.append(ret.get('n_var', 0))

				print("alpha = {}".format(m.alpha))
				print("beta = {}".format(m.beta))
				print("gamma = {}".format(m.gamma))
				print("k0 = {}".format(m.k0))
				print("tau = {}".format(m.tau))
				print("A0 = {}".format(ret['A0']))
				print("n = {}".format(ret['n']))
			A0[model] = _A0
			n[model] = _n
			n_var[model] = _n_var

		print_output(args, "Alpha/Gamma", "\\alpha/\\gamma", A0, n, O)

	if args.pnas:
		A0 = {}
		n = {}
		n_var = {}

		# beta = omega * alpha
		for model in args.models:
			Model = getattr(__import__(model), model)
			m = Model(conf)
			m.read_data()

			_A0 = []
			_n = []
			_n_var = []
			for omega in P:
				m.beta = m.alpha * omega
				ret = m.run(samples)
				_A0.append(ret['A0'])
				_n.append(ret['n'])
				_n_var.append(ret.get('n_var', 0))

			A0[model] = _A0
			n[model] = _n
			n_var[model] = _n_var	
			
		print_output(args, "Beta/Alpha", "\\beta/\\alpha", A0, n, P)	






