
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define the parameters and initial conditions
a = 1.0
b = 5.0
tau = 3.0
initCond = [1.0]  # Initial condition
time = np.linspace(0, 10, 100)  # Time array

# History to store Y values
Y_history = []

# Define the equation system with phase shift
def eqtnSystem(Y, t, time_history, a, b, tau):
    # Update the history of Y
    Y_history.append(Y[0])

    # Get the past time value for Y(t-tau)
    if len(time_history) > 0 and t - tau in time_history:
        Y_past = time_history(t - tau)
    else:
        Y_past = 0  # Default if no past value is available

    # Differential equation
    dYdt = a * Y[0] + b * Y_past
    return [dYdt]

# Method to create a time-based interpolation of history
def create_time_interpolator(Y_history, time_points):
    return interp1d(time_points, Y_history, fill_value="extrapolate")

# Initialize the odeint process
results = []
time_history = np.array([])

for t in time:
    # Create an interpolator with the latest history
    if len(Y_history) > 0:
        interpolator = create_time_interpolator(np.array(Y_history), time_history)
    else:
        interpolator = lambda x: 0  # No past values available

    # Solve the differential equation step by step
    result = odeint(eqtnSystem, initCond, [t], args=(interpolator, a, b))
    results.append(result[0, 0])  # Keep track of results

    # Update history for next time step
    time_history = np.append(time_history, t)

# Convert results to a numpy array for easier handling
results = np.array(results)

# You can access results here
print(results)
