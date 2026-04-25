
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define constants for your equation
a = 1
b = 5
tau = 3

# Initial conditions
initCond = [1.0]  # Example initial condition
time = np.linspace(0, 20, 200)  # Time vector

# Function to define the differential equations
def eqtnSystem(Y, t, past_times, past_values):
    # Interpolate to find Y(t - tau)
    if t - tau >= 0:
        Y_minus_tau = interp1d(past_times, past_values, fill_value="extrapolate")(t - tau)
    else:
        Y_minus_tau = Y  # If t - tau < 0, use current value (or some default)

    dYdt = a * Y + b * Y_minus_tau
    return dYdt

# History tracking
past_times = []
past_values = []

# Function to run the integration and collect past values
def run_integration():
    global past_times, past_values
    Y = initCond
    ETA = []

    for t in time:
        # Integrate using the previous value and current time
        if past_times:
            past_value = past_values[-1]
        else:
            past_value = Y

        Y = odeint(eqtnSystem, Y, [t], args=(past_times, past_values))[-1][0]
        ETA.append(Y)

        past_times.append(t)
        past_values.append(Y)

    return np.array(ETA)

# Perform integration
ETA = run_integration()

# Example output of specific components
print(ETA)
