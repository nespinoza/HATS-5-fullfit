import pickle
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_style('ticks')

P, t0 = 4.7633922397, 2459198.5136332442

posteriors = pickle.load(open('_dynesty_DNS_posteriors.pkl', 'rb'))
samples = posteriors['posterior_samples']

cycles = np.array([])
residuals = np.array([])
residuals_err = np.array([])

for k in list(samples.keys()):
    
    # T_p1_TESS5_-158
    if 'T_p1_' in k:

        cycle = int(k.split('_')[-1])
        delta_t = ( samples[k] - (t0 + P * cycle) ) * 24 * 60 # residuals to minutes

        cycles = np.append(cycles, cycle)
        residuals = np.append(residuals, np.median(delta_t))
        residuals_err = np.append( residuals_err, np.sqrt(np.var( delta_t )) ) 

        print(cycle, np.median(samples[k]), np.sqrt(np.var(samples[k])), t0 + (P*cycle))

plt.errorbar(cycles, residuals, residuals_err, fmt = 'o')
plt.show()
