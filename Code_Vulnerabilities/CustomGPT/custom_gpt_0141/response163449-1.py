
import numpy as np
from scipy.integrate import odeint

# Define the delay
tau = 3

# Initialize parameters
a = 1
b = 5

# Define the system of differential equations
def etaFunc(Y, t, past_vals):
    # Note that Y is the current state at time t
    # Retrieve previous state values for past (t - tau)
    if t > tau:
        # Interpolating to get the value of Y(t - tau)
        Y_past = past_vals[int(t - tau)]
    else:
        # If t is less than tau, we assume Y is zero or initialize as required
        Y_past = 0

    # Define the rate of change
    dYdt = a * Y + b * Y_past

    return dYdt

# This function will manage the past values for interpolation
def integrate_with_delay(init_cond, time):
    past_vals = np.zeros((len(time) + tau, len(init_cond)))  # Buffer for past values
    past_vals[0] = init_cond  # Initial conditions

    # Storage for simulation results
    results = np.zeros((len(time), len(init_cond)))

    for i, t in enumerate(time):
        # Using odeint for integration
        if i == 0:
            results[i] = init_cond
        else:
            # Store the past value before advancing t
            past_vals[i] = results[i-1]

        # Call the etaFunc to find the derivatives
        dydt = etaFunc(results[i], t, past_vals)

        # Store the new result in the results array
        results[i] = results[i - 1] + dydt  # Simple Euler step (can replace with integration method if desired)

    return results

# Define time points and initial conditions
time = np.linspace(0, 20, 100)  # 0 to 20 seconds, 100 points
init_cond = np.array([0])  # Assume initial value is 0

# Integrate the equations with delay
ETA = integrate_with_delay(init_cond, time)

# Now you can access each component of ETA
print(ETA)
