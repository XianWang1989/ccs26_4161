
import numpy as np
from scipy.integrate import odeint

# Function to retrieve past values based on interpolation
def pastEta(t, times, values):
    if t < times[0]:
        return values[0]  # Before the known range
    elif t > times[-1]:
        return values[-1]  # After the known range
    else:
        # Interpolate past values
        index = np.searchsorted(times, t, side='right') - 1
        return values[index]

# Euler's method to store solutions
def etaFunc(A, t, times, solutions):
    # Define constants
    gamma = np.array([[1, 2], [3, 4]])  # Replace with your actual values
    zeta = [0, 0, 0, 0, 0]  # Replace with your actual values
    tau = [1, 1, 1, 1]  # Replace with your actual values
    beta = np.array([[1, 1], [1, 1]])  # Replace with your actual values
    theta = [1, 2, 3, 4]  # Replace with your actual values

    # Current values of eta
    eta = A

    # Get past values based on interpolation
    past_eta_3 = pastEta(t - theta[3], times, solutions[:, 3])
    past_eta_4 = pastEta(t - theta[4], times, solutions[:, 4])

    # Return derivatives
    return np.array([
        (gamma[0, 0] - eta[0] + zeta[0]) / tau[0],
        (gamma[1, 1] - eta[1] + zeta[1]) / tau[1],
        (gamma[2, 2] - eta[2] + zeta[2]) / tau[2],
        (beta[3, 0] * past_eta_3 - eta[3] + zeta[3]) / tau[3],
        (beta[4, 3] * past_eta_4 - eta[4] + zeta[4]) / tau[4]
    ])

# Initial conditions and time points
initCond = [1, 2, 3, 4, 5]  # Replace with your actual initial conditions
time = np.linspace(0, 10, 100)  # Time points for the solution

# Store solutions
solutions = np.zeros((len(time), len(initCond)))

# Solve the equation using odeint
for i, t_val in enumerate(time):
    if i == 0:
        solutions[i] = initCond  # Using initial conditions
    else:
        time_interval = time[:i]  # Time points till now
        solutions[i] = odeint(lambda A, t: etaFunc(A, t, time_interval, solutions), solutions[i - 1], [t_val])[0]

# The result at time t can be accessed using solutions[i]
eta_0 = solutions[:, 0]
eta_1 = solutions[:, 1]
eta_2 = solutions[:, 2]
eta_3 = solutions[:, 3]
eta_4 = solutions[:, 4]
