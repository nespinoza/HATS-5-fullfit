import numpy as np
import juliet

dataset = juliet.load(priors='priors/priors.dat', lcfilename='data/lc.dat', rvfilename='data/rvs.dat', out_folder = 'full',\
                      GPlceparamfile='data/GP_lc_regressors.dat', verbose = True)

results = dataset.fit(sampler = 'dynamic_dynesty', n_live_points = 3000, nthreads = 4, \
                      ecclim = 0.5)
