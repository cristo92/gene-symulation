import sys
import argparse

ALL = ["PNAS", "DelayedSymulation", "EwaModel", "MyModel", "MiekiszSzymanska"]

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Stochastic simulation")
	parser.add_argument("config", help="Config file")
	parser.add_argument("-s", "--samples", type=int, help="Number of times simulation is ran. Result is mean value of all times.")
	parser.add_argument("models", help="Models which we're going to use.", nargs="+")

	args = parser.parse_args()

	conf = args.config
	samples = vars(args).get('samples', 1)

	T = [0, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1, 2.5, 5, 10, 50]
	
	A0 = {}
	n = {}
	if "all" in args.models:
		args.models = ALL
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

	print("============ A0 ============")
	print("Tau\t\t{}".format("\t".join([str(t) for t in T])))
	for model in args.models:
		_A0 = A0[model]
		print("{}{}{}".format(model[:15], "\t" * max(1, 2 - len(model)/8), 
		           "\t".join(["{:.3f}".format(t) for t in _A0])))
	print("============ n =============")
	print("Tau\t\t{}".format("\t".join([str(t) for t in T])))
	for model in args.models:
		_n = n[model]
		print("{}{}{}".format(model[:15], "\t" * max(1, 2 - len(model)/8), 
		           "\t".join(["{:.3f}".format(t) for t in _n])))
