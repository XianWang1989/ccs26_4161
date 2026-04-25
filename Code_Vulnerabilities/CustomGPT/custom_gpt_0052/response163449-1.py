
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1.0
b = 5.0
tau = 3.0

# Store past values
past_values = []

def past_eta(t, values):
    # Only return relevant past values
    return [v for t_v, v in values if t_v <= t]

def eqtn_system(Y, t):
    # Store current time and value in past values
    past_values.append((t, Y[0]))

    # Fetch past value for t - tau, ensuring we only consider valid past states
    past_Y = past_eta(t - tau, past_values)
    Y_tau = past_Y[-1] if past_Y else 0  # Use 0 if no past value is available

    # Define the system of ODEs
    dYdt = a * Y[0] + b * Y_tau
    return [dYdt]

# Initial conditions
init_cond = [1.0]
time = np.linspace(0, 20, 100)  # Time array

# Solve ODE
ETA = odeint(eqtn_system, init_cond, time)

# Get results
eta_0 = ETA[:, 0]

# Output the result for demonstration
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('Solution of the ODE with Phase Shift')
plt.grid(True)
plt.show()
