
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1.0
b = 5.0
tau = 3.0

# Function to compute the differential equation
def etaFunc(eta, t, past_values):
    # Update past values
    if t - tau >= 0:
        past_eta = past_values[int(t - tau)]
    else:
        past_eta = 0  # or some default value

    # Define the differential equations
    dEta_dt = np.zeros_like(eta)
    dEta_dt[0] = a * eta[0] + b * past_eta  # Example equation for eta[0]
    # Add more equations for other eta components as needed

    return dEta_dt

# Function to integrate over time
def integrate_system(init_cond, time):
    past_values = []

    # Initialize past values with the initial condition
    past_values.append(init_cond)

    # Store results during integration
    results = []

    for t in time:
        if len(past_values) > 1:
            past_values.append(results[-1])  # Append last computed value
        else:
            past_values.append(init_cond)  # First time point

        current_eta = odeint(etaFunc, past_values[-1], [t], args=(past_values,))[0]
        results.append(current_eta)

    return np.array(results)

# Initial conditions and time vector
init_cond = np.array([0.0])  # Initial conditions for whatever dimensions needed
time = np.linspace(0, 20, 100)

# Perform the integration
ETA = integrate_system(init_cond, time)

# Access individual components
eta_0 = ETA[:, 0]
print(eta_0)
