
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3
total_time = 10  # Total time for simulation
dt = 0.1  # Time step
time_points = np.arange(0, total_time, dt)

# Initialize past values
max_tau_points = int(tau / dt)
past_eta = np.zeros(max_tau_points)
indices = np.arange(max_tau_points)

def etaFunc(eta, t):
    # Shift and wrap the past values
    past_index = t // dt % max_tau_points
    past_value = past_eta[past_index] if t >= tau else 0

    # Calculate derivative
    d_eta_dt = a * eta + b * past_value
    return d_eta_dt

# Initial condition
initCond = [0]  # Initial value for eta

# Store history for past_eta
def update_past_values(current_eta, t):
    past_index = int(t // dt % max_tau_points)
    past_eta[past_index] = current_eta[0]

# Solve the differential equation
ETA = np.zeros((len(time_points), len(initCond)))

for i, t in enumerate(time_points):
    if i == 0:
        ETA[i] = initCond
    else:
        current_eta = odeint(etaFunc, ETA[i-1], [t - dt, t])
        ETA[i] = current_eta[1]

    # Update past values
    update_past_values(ETA[i], t)

# Accessing results
eta_0 = ETA[:, 0]

# Example plot (optional)
import matplotlib.pyplot as plt

plt.plot(time_points, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('Dynamics of eta_0 over time')
plt.legend()
plt.show()
