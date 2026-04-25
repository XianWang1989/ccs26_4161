
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Global storage for previously calculated values
past_eta = []

def etaFunc(A, t):
    # Parameters and constants
    gamma = np.array([[1, 0], [0, 1], [0, 0]])
    zeta = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    tau = [1.0, 1.0, 1.0, 3.0, 3.0]  # Example tau values
    theta = [1.0, 2.0, 3.0, 3.0, 3.0]  # Time shifts

    # Save current eta for interpolation
    global past_eta
    past_eta.append(A)

    # Get current time values for interpolation
    times = np.arange(len(past_eta))

    # Prepare output array
    out = np.zeros_like(A)

    for i in range(len(A)):
        if t - theta[i] >= 0 and len(past_eta) > 0:
            # Interpolate past values for Y(t-tau)
            past_times = np.arange(len(past_eta))
            past_func = interp1d(past_times, np.array(past_eta), axis=0, fill_value='extrapolate')
            out[i] = (gamma[i, i] * A[i] - A[i] + zeta[i]) / tau[i] + past_func(t - theta[i])[i] / tau[i]
        else:
            out[i] = (gamma[i, i] * A[i] - A[i] + zeta[i]) / tau[i]  # No past value available

    return out

# Initial conditions and time points
initCond = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
time = np.linspace(0, 10, 100)

# Solve the system
ETA = odeint(etaFunc, initCond, time)

# Access components
eta_0 = ETA[:, 0]
print(eta_0)
