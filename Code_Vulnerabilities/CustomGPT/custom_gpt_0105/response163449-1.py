
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define the parameters
a = 1
b = 5
tau = 3

# Time array
time = np.linspace(0, 20, 1000)

# Function for eta and its past values
def eta_func(t):
    # Example: define your function here
    return np.sin(t)

# Interpolating function to get past values
def past_eta(t, t_data, eta_data):
    # Ensure the time data is sorted
    return interp1d(t_data, eta_data, fill_value="extrapolate")(t)

# Define the differential equations
def eqtnSystem(Y, t, t_data, eta_data):
    Y_current = Y[0]
    Y_past = past_eta(t - tau, t_data, eta_data)  # Get past values using interpolation
    return [a * Y_current + b * Y_past]

# Initial conditions
init_cond = [eta_func(0)]
eta_data = [init_cond[0]]  # Store the initial value of eta
t_data = [0]  # Time data for interpolation

# Integrate the equations
ETA = []
for t in time:
    t_data.append(t)
    # Update eta_data
    if t > 0:
        eta_data.append(eta_func(t))  # Store current eta for later interpolation

    sol = odeint(eqtnSystem, init_cond, [t], args=(t_data, eta_data))
    ETA.append(sol[0])

ETA = np.array(ETA)

# Extract individual components
eta_0 = ETA[:, 0]

# Example plot (if needed)
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('eta')
plt.legend()
plt.show()
