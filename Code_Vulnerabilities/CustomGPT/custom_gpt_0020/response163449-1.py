
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1           # Coefficient a
b = 5           # Coefficient b
tau = 3         # Time shift

# To store the history of Y
history = []

def eqtnSystem(Y, t):
    # Input Y can be a list or np.ndarray, so we retrieve the latest value
    current_value = Y[0]

    # Store the current value for the history list
    history.append(current_value)

    # Get the value from 'tau' time units ago
    if t >= tau and len(history) > 0:
        past_value = history[-int(tau)]  # Get value stored 'tau' time steps back
    else:
        past_value = 0  # Default (or can use any initial condition)

    dYdt = a * current_value + b * past_value
    return [dYdt]

# Time points where solution is calculated
time = np.linspace(0, 30, 300)

# Initial condition
initCond = [1.0]  # Starting value of Y

# Solve the ODE
ETA = odeint(eqtnSystem, initCond, time)

# Extract the results
Y_values = ETA[:,0]

# Now you can analyze or plot Y_values
import matplotlib.pyplot as plt

plt.plot(time, Y_values)
plt.title('Solution to the ODE with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.grid()
plt.show()
