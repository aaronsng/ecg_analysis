from __future__ import print_function
import matplotlib.pyplot as plt
import wfdb
import numpy as np
import scipy.signal as signal
import heartpy as hp
from scipy.signal import firwin

LEAD = 1

record = wfdb.rdsamp('st-petersburg-incart-12-lead-arrhythmia-database-1.0.0/files/I01')
annotation = wfdb.rdann('st-petersburg-incart-12-lead-arrhythmia-database-1.0.0/files/I01', 'atr')
t = np.copy(np.array(record[0][:, LEAD]))
b = firwin(513, 0.5, width=0.05, pass_zero='highpass')
filtered = hp.remove_baseline_wander(t, 257, 0.05) #high pass filter
filtered = hp.filter_signal(filtered, cutoff=30, sample_rate=257.0, order=4) #low pass filter
filtered_t = np.array([np.convolve(xi, b, mode='valid') for xi in t])
#plt.plot(filtered)
#plt.show()

wd, m = hp.process(hp.scale_data(filtered), sample_rate=257)

plt.figure(figsize=(12, 4))
plot_object = hp.plotter(wd, m)

for measure in m.keys():
    print('%s: %f' % (measure, m[measure]))



