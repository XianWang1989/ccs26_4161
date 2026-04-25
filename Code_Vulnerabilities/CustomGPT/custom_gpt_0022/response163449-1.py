
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a = 1
b = 5
tau = 3

# History array for past values of Y
history_length = 20  # Adjust as needed based on tau
history = np.zeros(history_length)

def eqtnSystem(Y, t, history):
    # Update history to include the latest value
    if len(history) > 0:
        history[:-1] = history[1:]  # Shift history
        history[-1] = Y  # Append the latest Y in history

    past_index = int(tau)  # Using tau as the time delay index

    # Retrieve past value using phase shift
    past_Y = history[-past_index] if t >= tau else 0

    # Calculate dY/dt
    dYdt = a * Y + b * past_Y
    return dYdt

# Time points where solution is computed
time = np.linspace(0, 20, 100)
initCond = 1.0

# Integrate the ODE
ETA = np.zeros((len(time), 1))
ETA[0] = initCond

for i in range(1, len(time)):
    t_current = time[i]
    ETA[i] = odeint(eqtnSystem, ETA[i-1], [t_current], args=(history,))[-1]

# Plot the results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Solution of dY/dt with Phase Shift')
plt.grid()
plt.show()
