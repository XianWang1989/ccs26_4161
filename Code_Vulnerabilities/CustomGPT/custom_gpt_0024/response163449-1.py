
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a = 1.0
b = 5.0
tau = 3.0
time_steps = 100
time = np.linspace(0, 20, time_steps)

# Initialize values
initCond = [0]  # Initial condition for Y
eta_history = []

def eqtnSystem(Y, t, eta_history):
    if t >= tau:
        # Get the index for the past value (Y(t-tau))
        past_index = np.searchsorted(time, t - tau) - 1
        past_value = eta_history[past_index] if past_index >= 0 else 0
    else:
        past_value = 0  # Default value before tau

    # Store current value for the history
    eta_history.append(Y[0])

    return [a * Y[0] + b * past_value]

# Integrate the system
ETA = odeint(eqtnSystem, initCond, time, args=(eta_history,))

# Plotting the result
plt.plot(time, ETA)
plt.title('Solution of Differential Equation with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.grid()
plt.show()
