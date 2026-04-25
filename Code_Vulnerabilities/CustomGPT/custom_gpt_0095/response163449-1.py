
import numpy as np
from scipy import integrate
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Parameters
a = 1
b = 5
tau = 3

# Time span
start_time = 0
end_time = 20
time = np.linspace(start_time, end_time, 100)  # 100 time points

# Initial conditions
initCond = [1, 0, 0, 0, 0]  # Example initial conditions for eta

# Store computed values for interpolation
eta_history = []

def etaFunc(Y, t):
    global eta_history  # Access global history of eta values

    # Record current eta
    eta_history.append(Y.copy())

    # Prepare for interpolation
    past_times = np.array([t_i for t_i in time if t_i < t])
    if len(eta_history) > 1:
        past_values = np.array(eta_history)
        interp_func = interp1d(past_times, past_values, axis=0, fill_value="extrapolate")

        past_eta = interp_func(t - tau)
    else:
        past_eta = np.zeros_like(Y)  # Initialize if no past values

    # Differential equations
    dydt = np.array([a * Y[0] + b * past_eta[0],
                     a * Y[1] + b * past_eta[1],
                     a * Y[2] + b * past_eta[2],
                     a * Y[3] + b * past_eta[3],
                     a * Y[4] + b * past_eta[4]])
    return dydt

# Integrate using odeint
ETA = integrate.odeint(etaFunc, initCond, time)

# Plot results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('ETA Components')
plt.title('ETA Over Time with Phase Shift')
plt.legend(['eta_0', 'eta_1', 'eta_2', 'eta_3', 'eta_4'])
plt.show()
