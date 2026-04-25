
import numpy as np
from scipy.integrate import odeint

# Initialize parameters
a = 1
b = 5
tau = 3
time_steps = 100  # Total time steps for simulation
time = np.linspace(0, 20, time_steps)  # Time array
init_cond = np.zeros(5)  # Initial condition for 5 variables

# Store the history of eta values
eta_history = []

def pastEta(t, history, tau):
    # Return the interpolated value from history for t-tau
    if t < tau:
        return 0  # No past value available
    else:
        # Find previous times
        t_values = np.array([h[0] for h in history])
        if t - tau in t_values:
            return history[t_values == (t - tau)][0][1]  # Exact past value
        else:
            # Interpolate if no exact match
            return np.interp(t - tau, t_values, [h[1] for h in history])

def etaFunc(A, t):
    global eta_history
    # Calculate current eta values
    eta = np.array(A)

    # Store current time and eta for history
    eta_history.append((t, eta.copy()))

    # Calculate dY/dt incorporating past values
    return np.array([
        a * eta[0] + b * pastEta(t, eta_history, tau),
        a * eta[1],
        a * eta[2],
        (beta[3, 0] * pastEta(t - theta[3], eta_history, tau) + 
         beta[3, 1] * pastEta(t - theta[4], eta_history, tau) - eta[3]) / tau,
        (beta[4, 3] * pastEta(t - theta[6], eta_history, tau) - 
         eta[4]) / tau
    ])

# Integrate the differential equations
ETA = odeint(etaFunc, init_cond, time)

# Access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# etc.

# Plot results or further analysis...
