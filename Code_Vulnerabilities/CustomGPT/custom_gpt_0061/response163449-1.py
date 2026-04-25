
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define parameters
a = 1
b = 5
tau = 3

# Define the system of equations
def eqtnSystem(Y, t, past_values):
    # Interpolating the past values of Y
    Y_interp = interp1d(past_values['time'], past_values['Y'], fill_value='extrapolate')
    Y_tau = Y_interp(t - tau)  # Y(t - tau)

    # Define the differential equation
    dYdt = a * Y + b * Y_tau
    return dYdt

# Time vector
time = np.linspace(0, 20, 100)

# Initial condition
initCond = np.array([1.0])  # Starting value of Y

# Store past values for interpolation
past_values = {'time': [], 'Y': []}

# Define a function to store history for interpolation
def save_history(t, Y):
    past_values['time'].append(t)
    past_values['Y'].append(Y)

# Create the function that includes saving history
def etaFunc(Y, t):
    save_history(t, Y[0])  # Save history
    return eqtnSystem(Y, t, past_values)

# Integrate the system
ETA = odeint(etaFunc, initCond, time)

# Retrieve individual components
eta_0 = ETA[:, 0]

# Plotting
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('Solution of the Differential Equation with Phase Shift')
plt.show()
