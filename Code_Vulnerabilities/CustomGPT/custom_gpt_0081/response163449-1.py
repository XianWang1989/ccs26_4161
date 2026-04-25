
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Time settings
time = np.linspace(0, 10, 1000)  # Time array from 0 to 10 with 1000 points
dt = time[1] - time[0]            # Time step

# Initial conditions
initCond = [0]  # Example initial condition for Y

# Function to define the differential equations
def eqtnSystem(Y, t, history):
    Y_current = Y[0]

    # Determine the index of the past value in the history (shift by tau)
    past_index = int(np.floor(tau/dt))

    # Get the past Y value, ensuring we do not exceed the bounds of the history
    if t - tau >= time[0]:  # Check if the past value exists in history
        Y_past = history[max(0, len(history)-past_index-1)]  # At time t-tau
    else:
        Y_past = 0  # If it's before our starting time, use some default value (e.g., 0)

    # Calculate dY/dt
    dYdt = a * Y_current + b * Y_past
    return [dYdt]

# Function to run the integration
def run_integration():
    # Create an empty list to store history
    history = []

    # Results array
    results = []

    for t in time:
        # Integrate equations using previous history values
        Y = eqtnSystem(initCond, t, history)
        results.append(Y[0])  # Store current result

        # Add the newly calculated Y to history
        history.append(initCond[0])
        # Update initial condition for next time step
        initCond[0] = Y[0]

    return np.array(results)

# Run the integration
ETA = run_integration()

# Plot the results (if needed)
import matplotlib.pyplot as plt

plt.plot(time, ETA, label='Y(t)')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.title('dY/dt with Phase Shift')
plt.legend()
plt.show()
