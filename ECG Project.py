from __future__ import print_function
import matplotlib.pyplot as plt
import wfdb
import numpy as np
import scipy.signal as signal
import heartpy as hp
from scipy.signal import firwin

LEAD = 1

record = wfdb.rdsamp('incartdb/1.0.0/I01')
annotation = wfdb.rdann('incartdb/1.0.0/I01', 'atr')
t = np.copy(np.array(record[0][:, LEAD]))
b = firwin(513, 0.5, width=0.05, pass_zero='highpass')
filtered = hp.remove_baseline_wander(t, 257, 0.05) #high pass filter
filtered = hp.filter_signal(filtered, cutoff=30, sample_rate=257.0, order=4) #low pass filter
filtered_t = np.array([np.convolve(xi, b, mode='valid') for xi in t])
#plt.plot(filtered)
#plt.show()

wd, m = hp.process(hp.scale_data(filtered), sample_rate=257)

plt.figure(figsize=(12, 4))
#plot_object = hp.plotter(wd, m)
for i in range(100, 200, 10):
    beat_1 = wd['RR_indices'][i]
    beat_2 = wd['RR_indices'][i + 1]

    start_1 = beat_1[0]
    end_1 = beat_1[1]

    start_2 = beat_2[0]
    end_2 = beat_2[1]
    ecg1 = filtered[int((end_1 + start_1) / 2):int((end_2 + start_2) / 2)]
    plt.plot(ecg1)
    plt.show()
# # print(wd['RR_indices'][100]
# print(wd.keys())
# for measure in m.keys():
#     print('%s: %f' % (measure, m[measure]))