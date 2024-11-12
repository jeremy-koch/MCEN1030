# the code in this file below simulates real-time data collection and should be left unchanged
import numpy as np

def thermal_data(T,Q):
    if np.random.randint(1,40) == 8:
        return T-np.random.randint(1,20)
    else:
        return T+0.2*Q+0.5*np.random.normal()-0.5
