
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Parameters
a = 1
b = 5
tau = 3

# Time settings
time = np.linspace(0, 20, 200)  # Time array
initCond = [1]  # Initial condition for Y

# Function to define the differential equations
def eqtnSystem(Y, t, Y_past):
    current_Y = Y[0]
    # Interpolating Y values
    if t - tau >= 0:
        Y_past_func = interp1d(time[:len(Y_past)], Y_past, fill_value="extrapolate")
        past_Y = Y_past_func(t - tau)
    else:
        past_Y = 0  # Or some other value if not available

    return [a * current_Y + b * past_Y]

# Store results for Y
Y_history = []

# Main calculation loop
def run_simulation():
    global Y_history
    # Integrate using odeint
    for i, t_val in enumerate(time):
        if i == 0:
            Y_history.append(initCond[0])
            continue

        # Calculate the new value for Y
        current_Y = odeint(eqtnSystem, [Y_history[-1]], [t_val], args=(Y_history,))[0][0]
        Y_history.append(current_Y)

run_simulation()

# Convert historical values to a numpy array for use
Y_history = np.array(Y_history)

# Plotting the results
import matplotlib.pyplot as plt
plt.plot(time, Y_history)
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('Solution of the Differential Equation with Phase Shift')
plt.grid()
plt.show()
