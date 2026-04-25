
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define the parameters
a = 1
b = 5
tau = 3

# Storage for historical data
history_time = []
history_Y = []

def model(Y, t):
    global history_time, history_Y

    # Add current time and state to history
    history_time.append(t)
    history_Y.append(Y)

    # Interpolation for the past value Y(t - tau)
    if t >= tau:
        interp_func = interp1d(history_time, history_Y, fill_value="extrapolate")
        past_Y = interp_func(t - tau)
    else:
        past_Y = 0  # Or handle as needed for t < tau

    # Define the differential equation
    dYdt = a * Y + b * past_Y
    return dYdt

# Initial conditions and time points
initCond = [1.0]  # Initial value for Y
time = np.linspace(0, 20, 200)

# Perform integration
ETA = odeint(model, initCond, time)

# Extract results
eta0 = ETA[:, 0]

# You can plot or further analyze eta0 as needed
import matplotlib.pyplot as plt

plt.plot(time, eta0)
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Solution of the ODE with Phase Shift')
plt.show()
