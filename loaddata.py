import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin
import heartpy

LEAD = 2

record = wfdb.rdsamp('incartdb/1.0.0/I01')
annotation = wfdb.rdann('incartdb/1.0.0/I01', 'atr')
t = np.copy(np.array(record[0][1000:,LEAD]))
# print(annotation)

filtered = heartpy.remove_baseline_wander(t, 257, cutoff=0.05) # HIGH PASS
filtered = heartpy.filter_signal(filtered, cutoff=30, sample_rate=257.0, order=4) # LOW PASS
# b = firwin(513, 0.5, width=0.05, pass_zero='highpass') 
# filtered_t = np.array([np.convolve(xi, b, mode='valid')[4] for xi in t])
plt.plot(filtered)
plt.show()

def load_visualise(data, annotations):
    '''
    loads data and annotations, plots them 
    and returns data and annotations
    '''

    #explore signal
    plt.figure(figsize=(12,3))
    plt.plot(data)
    plt.scatter(annotations, [data[int(x)] for x in annotations], color='green')
    plt.show()

    #and zoom in
    plt.figure(figsize=(12,3))
    plt.plot(data)
    plt.scatter(annotations, [data[int(x)] for x in annotations], color='green')
    plt.xlim(20000, 26000)
    plt.show()

    return data, annotations

# ecg, annotations = load_visualise(filtered, annotation)