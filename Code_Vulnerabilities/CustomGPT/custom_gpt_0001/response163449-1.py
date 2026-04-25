
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Sampling time
t = np.linspace(0, 20, 100)  # Time from 0 to 20 seconds, 100 points
dt = t[1] - t[0]

# Parameters
a = 1
b = 5
tau = 3

# Create a global list to store past values of Y
history = []

def ode_system(Y, t):
    """ 
    ODE system with time-delayed feedback 
    """
    # Ensure history is long enough to fetch `Y(t-tau)`
    if len(history) <= int(t / dt) + 1:
        history.append(Y[0])  # Store the current value for history

    # Fetch the previous value based on the time shift
    Y_tau = history[int((t - tau) / dt)] if t - tau >= 0 else 0  # Zero if the shift is negative
    dYdt = a * Y[0] + b * Y_tau
    return [dYdt]

# Initial condition
init_cond = [0]  # Initial value of Y

# Solve ODE
Y_sol = odeint(ode_system, init_cond, t)

# Plotting the results
plt.plot(t, Y_sol[:, 0], label='Y(t)')
plt.xlabel('Time')
plt.ylabel('Y')
plt.title('Dynamic system with phase shifted reaction')
plt.legend()
plt.grid()
plt.show()
