
import numpy as np
from scipy.integrate import odeint

# Global list to keep track of past values of eta
history = []

def etaFunc(A, t):
    # Constants
    gamma = np.array([[1, 0], [0, 1], [0, 0]])
    beta = np.array([[0.5, 0.2], [0.3, 0.7]])
    zeta = np.zeros(5)
    theta = np.array([1, 2, 3, 1, 2, 3])
    tau = np.array([1, 1, 1, 1, 1])

    # Maintain history of eta
    history.append(A)

    # Previous eta values based on time shifts
    def pastEta(t):
        if t < 0 or len(history) == 0:
            return np.zeros(len(A))  # Return zeros if there's no past value
        index = int(len(history) - (t / 0.1))  # Assuming time steps of 0.1
        index = max(0, min(index, len(history) - 1))  # Keep index within bounds
        return history[index]

    # Calculate derivatives
    dA_dt = np.zeros_like(A)
    for i in range(len(A)):
        dA_dt[i] = (gamma[i, i] * A[i] - A[i] + zeta[i]) / tau[i]

    # Include past values for `eta3` and `eta4`
    dA_dt[3] = (beta[3, 0] * pastEta(t - theta[3])[0] +
                 beta[3, 1] * pastEta(t - theta[4])[1] +
                 beta[3, 2] * pastEta(t - theta[5])[2] - A[3] + zeta[3]) / tau[3]

    dA_dt[4] = (beta[4, 3] * pastEta(t - theta[6])[3] +
                 beta[4, 2] * pastEta(t - theta[7])[2] - A[4] + zeta[4]) / tau[4]

    return dA_dt

# Time array
time = np.linspace(0, 10, 100)  # from 0 to 10, 100 time points

# Initial conditions
initCond = np.zeros(5)  # Initial values of eta

# Solve ODE
ETA = odeint(etaFunc, initCond, time)

# Extract individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
