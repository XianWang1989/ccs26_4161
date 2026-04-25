
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Simulation parameters
time = np.linspace(0, 20, 100)  # Time from 0 to 20 with 100 steps
initCond = np.zeros(5)  # Initial conditions for eta

# Constants (example values)
gamma = np.array([[1, 0], [0, 1], [1, 0]])
beta = np.array([[1, 0], [0, 1], [1, 0], [1, 1]])
tau = [1, 1, 1, 1, 1]
theta = [3, 3, 3, 3, 3]

# Store computed eta values
eta_values = []

def etaFunc(A, t):
    # Store the current value
    eta_values.append(A.copy())

    # Interpolation function
    past_times = np.linspace(0, len(eta_values)-1, len(eta_values))
    interpolator = interp1d(past_times, eta_values, bounds_error=False, fill_value=0)

    # Get past eta values
    if len(eta_values) > 0:
        t_past = (t - theta[0]) / (time[1] - time[0])
        past_eta = interpolator(t_past)
    else:
        past_eta = np.zeros_like(A)

    # Define the rate of change
    return np.array([
        (gamma[0, 0] * A[0] - A[0] + 1) / tau[0],
        (gamma[1, 1] * A[1] - A[1] + 1) / tau[1],
        (gamma[2, 2] * A[2] - A[2] + 1) / tau[2],
        (beta[3, 0] * past_eta[0] + beta[3, 1] * past_eta[1] - A[3] + 1) / tau[3],
        (beta[4, 3] * past_eta[3] - A[4] + 1) / tau[4]
    ])

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time)

# Now, you can access each component of ETA
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# and so on...
