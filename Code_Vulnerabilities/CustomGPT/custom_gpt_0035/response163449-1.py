
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3
time = np.linspace(0, 20, 100)  # Time range
initCond = [0]  # Initial condition

# Buffer size based on maximum delay
buffer_size = int(tau // (time[1] - time[0])) + 1
past_eta_buffer = np.zeros((buffer_size, len(initCond)))

def eqtn_system(Y, t, past_eta):
    # Update past_eta buffer
    past_eta[1:] = past_eta[:-1]  # Shift old values
    past_eta[0] = Y[0]  # Store current value
    Y_tau = past_eta[min(int(tau // (time[1] - time[0])), len(past_eta)-1)]  # Get delayed value
    return [a * Y[0] + b * Y_tau]

# Integrate
ETA = np.zeros((len(time), len(initCond)))  # Prepare output array
ETA[0] = initCond

for i in range(1, len(time)):
    t_span = [time[i-1], time[i]]
    sol = odeint(eqtn_system, ETA[i-1], t_span, args=(past_eta_buffer,))
    ETA[i] = sol[-1]

# Now you can access individual components as needed
eta_0 = ETA[:, 0]
