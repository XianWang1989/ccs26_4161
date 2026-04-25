
import numpy as np
from scipy import integrate
from scipy.interpolate import interp1d

# Example constants for demonstration
gamma = np.array([[1]], dtype=float)
beta = np.array([[1, 2], [3, 4]], dtype=float)
tau = np.array([1, 2, 3, 4, 5])
theta = np.array([1, 2, 3, 4, 5])
initCond = [0, 0, 0, 0, 0]
time = np.linspace(0, 10, 100)  # Time span

# Store past values of eta
eta_history = []

def pastEta(t):
    if len(eta_history) == 0 or t < 0:
        return [0, 0, 0]  # Return zeros if there is no history yet
    else:
        # Interpolation for past values
        interp = interp1d(time[:len(eta_history)], eta_history, fill_value="extrapolate", axis=0)
        return interp(t)

def etaFunc(A, t):
    global eta_history
    # Append current state to history
    eta_history.append(A)

    # Calculate eta based on the provided example
    return np.array([
        (gamma[0, 0] * xi(t - theta[0]) - A[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * xi(t - theta[1]) - A[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * xi(t - theta[2]) - A[2] + zeta[2]) / tau[2],
        (beta[3, 0] * pastEta(t - theta[3])[0] +
         beta[3, 1] * pastEta(t - theta[4])[1] +
         beta[3, 2] * pastEta(t - theta[5])[2] - A[3] + zeta[3]) / tau[3],
        (beta[4, 3] * pastEta(t - theta[6])[3] +
         beta[4, 2] * pastEta(t - theta[7])[2] - A[4] + zeta[4]) / tau[4],
    ])

# Example of running the ODE solver
ETA = integrate.odeint(etaFunc, initCond, time)

# Access individual components of ETA
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
