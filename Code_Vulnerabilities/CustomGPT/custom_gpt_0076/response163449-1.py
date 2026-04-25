
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Time history for previous values
history_length = 100
past_Y_values = np.zeros(history_length)

# Function to retrieve past values based on time shift
def get_past_value(t, t_shift, current_time_list, past_Y):
    if t - t_shift < 0:
        return 0  # Return 0 or any other boundary condition for t < 0
    else:
        # Find the index for the requested past time
        for i in range(len(current_time_list)-1):
            if current_time_list[i] <= t - t_shift < current_time_list[i+1]:
                return past_Y[i]
    return 0  # Default if not found

# Main system of equations
def eqtnSystem(Y, t, current_time_list, past_Y):
    Y_current = Y[0]
    Y_past = get_past_value(t, tau, current_time_list, past_Y)

    dYdt = a * Y_current + b * Y_past
    return [dYdt]

# Time points for the simulation
time = np.linspace(0, 10, 100)
init_cond = [1]  # Initial condition

# History of time points
current_time_list = np.linspace(0, 10, len(time))

# Solve the ODE
ETA = odeint(eqtnSystem, init_cond, time, args=(current_time_list, past_Y_values))

# Store the current values for future reference
for i in range(len(time)):
    if i < history_length:
        past_Y_values[i] = ETA[i, 0]

# Accessing individual components
eta_0 = ETA[:, 0]

# Example of how to plot or use eta_0
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.xlabel('Time')
plt.ylabel('ETA')
plt.title('Solutions of the Differential Equations')
plt.grid()
plt.show()
