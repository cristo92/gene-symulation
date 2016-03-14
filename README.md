# gene-symulation
Gene symulation in delayed production model.

# Usage
      Runner.py [-h] [-s SAMPLES] config models [models ...]

positional arguments:

      config                Config file
  
      models                Models which we're going to use.

optional arguments:

     -h, --help            show this help message and exit
  
     -s SAMPLES, --samples SAMPLES    Number of times simulation is ran. Result is mean value of all times.
                        
example:

      python Runner.py 1.conf DelayedSymulation -s 10
  
# Config File
Every config file should look like this:

      alpha	= 30
      beta	= 30
      k0	= 10
      k1	= 0
      gamma	= 1
      tau	= 5.0
      t_max	= 300
      t_const = 90
      n_beg	= 0
      dna_beg	= 0

