
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Parameters
a = 1
b = 5
tau = 3

# Initialize storage for past results
past_times = []
past_values = []

def etaFunc(A, t):
    global past_times, past_values

    # Store current time and value
    past_times.append(t)
    past_values.append(A)

    # Create an interpolation function for past values
    if len(past_times) > 1:
        interp_func = interp1d(past_times, past_values, axis=0, bounds_error=False, fill_value="extrapolate")
        Y_tau = interp_func(t - tau)  # Y(t-tau)
    else:
        Y_tau = 0  # If no past values, use a default value

    dA_dt = a * A + b * Y_tau
    return dA_dt

# Initial conditions
init_cond = [1.0]  # Starting value for Y
time = np.linspace(0, 20, 100)  # Time vector from 0 to 20

# Solve the differential equation
ETA = odeint(etaFunc, init_cond, time)

# Access specific components of ETA
eta_0 = ETA[:, 0]

# Example of plotting results (optional)
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('Value of eta_0')
plt.legend()
plt.show()
