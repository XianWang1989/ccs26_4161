
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Parameters
a = 1
b = 5
tau = 3
time = np.linspace(0, 50, 500)  # time array for integration
initCond = [1]  # Initial condition for Y

# Previous values storage
Y_history = []

# System of equations with phase shift
def eqtnSystem(Y, t):
    # Store the current value
    Y_history.append(Y[0])

    # Only use values from Y_history that are relevant
    if t - tau >= 0:
        Y_interp = interp1d(time[:len(Y_history)], Y_history, fill_value='extrapolate')
        Y_delayed = Y_interp(t - tau)
    else:
        Y_delayed = 0  # or some suitable value

    dYdt = a * Y[0] + b * Y_delayed
    return [dYdt]

# Solve the ODE using odeint
ETA = odeint(eqtnSystem, initCond, time)

# Extract result
eta_0 = ETA[:, 0]

# Display results
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='Y(t)', color='blue')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Differential Equation with Phase Shift')
plt.legend()
plt.show()
