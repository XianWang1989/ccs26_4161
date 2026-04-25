
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a = 1
b = 5
tau = 3

# Time parameters
start_time = 0
end_time = 20
num_points = 200
time = np.linspace(start_time, end_time, num_points)

# Constants and Initial Conditions
init_cond = [1]  # Initial value of Y(t)

# Create a buffer to store past values of Y
past_values_length = int(2 * tau)  # Buffer for two tau periods
past_values = np.zeros(past_values_length)

def eqtnSystem(Y, t, past_values):
    # Store current value in the past_values buffer
    past_values[1:] = past_values[:-1]  # Shift the past values
    past_values[0] = Y[0]  # Current value

    # Phase shift handling
    if t >= tau:
        past_Y_tau = past_values[int(tau / (end_time / num_points))]  # Get Y(t-tau)
    else:
        past_Y_tau = 0  # Y(t-tau) is not defined for t < tau

    # Return the derivative
    dYdt = a * Y[0] + b * past_Y_tau
    return [dYdt]

# Resulting storage for ETA
ETA = np.zeros((num_points, len(init_cond)))

# Integrating using odeint
for i in range(num_points):
    if i == 0:
        ETA[i] = odeint(eqtnSystem, init_cond, [time[i]], args=(past_values,))[0]
    else:
        ETA[i] = odeint(eqtnSystem, ETA[i-1], [time[i]], args=(past_values,))[0]

# Plotting the results
plt.plot(time, ETA[:, 0], label='Y(t)')
plt.title('Solution to the Differential Equation with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.legend()
plt.grid()
plt.show()
