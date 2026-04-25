
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Example parameters
gamma = np.array([[1], [1], [1]])
tau = np.array([1, 1, 1, 1, 1])
theta = np.array([1, 1, 1, 1, 1])
beta = np.random.rand(5, 5)  # Random coefficients for beta

# Global list to store past eta values
past_eta = []

def etaFunc(A, t):
    global past_eta

    # Append current value of A to past eta history
    past_eta.append(A.copy())

    # Interpolation for past values
    past_times = np.arange(len(past_eta))  # Time steps for stored eta
    results = []

    for i in range(len(A)):
        if t - theta[i] > 0:  # Check if the time is valid for interpolation
            past_value = np.interp(t - theta[i], past_times, [eta[i] for eta in past_eta])
        else:
            past_value = 0  # or any boundary condition
        results.append(past_value)

    # Example of dY/dt equation
    dA_dt = np.array([
        (gamma[0, 0] * results[0] - A[0]) / tau[0],
        (gamma[1, 1] * results[1] - A[1]) / tau[1],
        (gamma[2, 2] * results[2] - A[2]) / tau[2],
        (beta[3, 0] * results[0] + beta[3, 1] * results[1] - A[3]) / tau[3],
        (beta[4, 3] * results[3] + beta[4, 2] * results[2] - A[4]) / tau[4]
    ])

    return dA_dt

# Initial conditions and time
initCond = np.zeros(5)  # Initial conditions for eta
time = np.linspace(0, 10, 100)  # Time vector

# Integrate
ETA = odeint(etaFunc, initCond, time)

# Plot results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('ETA')
plt.title('ETA over time')
plt.legend([f'eta_{i}' for i in range(ETA.shape[1])])
plt.show()
