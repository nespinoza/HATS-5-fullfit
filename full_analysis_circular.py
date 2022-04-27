import numpy as np
import juliet

dataset = juliet.load(priors='priors/priors_circular.dat', lcfilename='data/lc.dat', rvfilename='data/rvs.dat', out_folder = 'full_circular',\
                      GPlceparamfile='data/GP_lc_regressors.dat', verbose = True)

results = dataset.fit(sampler = 'dynamic_dynesty', n_live_points = 3000, bound = 'single', sample = 'rwalk', nthreads = 4, \
                      ecclim = 0.5)
