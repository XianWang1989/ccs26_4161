
import numpy as np
from scipy.integrate import odeint

# Function to interpolate past values
def interpolate_past_values(time, values, t_current, tau):
    if t_current - tau < time[0]:  # Check if the past time is out of bounds
        return values[0]  # Return the first value if out of bounds
    return np.interp(t_current - tau, time, values)

# Example system definition
def etaFunc(A, t):
    # Example parameters
    gamma = np.array([[1, 1], [1, 1], [1, 1]])
    zeta = [1, 1, 1, 1, 1]
    tau = [1, 1, 1, 1, 1]
    theta = [1, 2, 3, 3, 3]
    beta = np.random.rand(5, 5)  # Random coefficient array for example

    # Time vector for interpolation (you'll need to store past values)
    past_time = np.linspace(0, 10, 100)  # Adjust based on your simulation
    past_eta_values = np.zeros((100, len(A)))  # Replace with actual computed values

    return np.array([
        (gamma[0, 0] * interpolate_past_values(past_time, past_eta_values[:, 0], t, theta[0]) - A[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * interpolate_past_values(past_time, past_eta_values[:, 1], t, theta[1]) - A[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * interpolate_past_values(past_time, past_eta_values[:, 2], t, theta[2]) - A[2] + zeta[2]) / tau[2],
        (beta[3, 0] * interpolate_past_values(past_time, past_eta_values[:, 0], t, theta[3]) +
         beta[3, 1] * interpolate_past_values(past_time, past_eta_values[:, 1], t, theta[4]) +
         beta[3, 2] * interpolate_past_values(past_time, past_eta_values[:, 2], t, theta[5]) - A[3] + zeta[3]) / tau[3],
        (beta[4, 3] * interpolate_past_values(past_time, past_eta_values[:, 3], t, theta[6]) +
         beta[4, 2] * interpolate_past_values(past_time, past_eta_values[:, 2], t, theta[7]) - A[4] + zeta[4]) / tau[4]
    ])

# Initial conditions and time setup
initCond = [0, 0, 0, 0, 0]
time = np.linspace(0, 10, 100)
ETA = odeint(etaFunc, initCond, time)

# To access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
eta_2 = ETA[:, 2]
