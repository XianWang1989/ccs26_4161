
import numpy as np
from scipy.integrate import odeint

# Define parameters
a = 1
b = 5
tau = 3

# Define the differential equation system
def eqtnSystem(Y, t, history):
    # Save current state to history
    if len(history) < 2:  # Avoid out-of-bounds access
        history.append(Y)
    else:
        history.pop(0)  # Remove oldest entry
        history.append(Y)

    # Retrieve Y(t-tau)
    # Interpolate if needed
    if t - tau < 0:
        Y_tau = 0  # Assuming zero for t < tau
    else:
        # Find appropriate past value, estimating if necessary
        idx = max(0, int(t - tau))
        if idx < len(history):
            Y_tau = history[idx]
        else:
            Y_tau = history[-1]  # Last known value

    return a * Y + b * Y_tau

# Set initial conditions and time points
initCond = [0]  # Initial condition
time = np.linspace(0, 20, 100)  # Time points for integration
history = []

# Call odeint with the history accumulator
ETA = odeint(eqtnSystem, initCond, time, args=(history,))

# Extract results
eta_0 = ETA[:, 0]

# For verification (plotting)
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='ETA')
plt.xlabel('Time')
plt.ylabel('ETA Values')
plt.title('Solution of the Differential Equation with Phase Shift')
plt.legend()
plt.show()
