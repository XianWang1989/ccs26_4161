
import numpy as np
from scipy.integrate import odeint

class PastValues:
    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.append(value)

    def get(self, t, tau):
        # Return the last value with delay tau
        if len(self.values) == 0 or t < tau:
            return 0  # or some default value
        return self.values[-int(tau)]  # use negative indexing

def eta_func(Y, t, past_values, theta, gamma, beta, zeta, tau):
    eta = Y
    # Calculate current values based on past values
    eta_past3 = past_values.get(t, theta[3])
    eta_past4 = past_values.get(t, theta[4])
    eta_past5 = past_values.get(t, theta[5])

    dydt = np.array([
        (gamma[0, 0] * xi(t - theta[0]) - eta[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * xi(t - theta[1]) - eta[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * xi(t - theta[2]) - eta[2] + zeta[2]) / tau[2],
        (beta[3, 0] * eta_past3 + beta[3, 1] * eta_past4 + beta[3, 2] * eta[2] - eta[3] + zeta[3]) / tau[3],
        (beta[4, 3] * eta_past4 + beta[4, 2] * eta_past5 - eta[4] + zeta[4]) / tau[4]
    ])

    # Update past values
    past_values.add(Y)
    return dydt

def xi(t):
    # Example xi function, replace with your own logic
    return np.sin(t)

# Constants
theta = [1, 2, 3, 4, 5, 6]  # Example values
gamma = np.eye(3)  # Example gamma matrix
beta = np.random.rand(5, 5)  # Example beta matrix
zeta = np.random.rand(5)  # Example zeta vector
tau = [1, 2, 3, 4, 5]  # Example tau values
init_cond = np.zeros(5)  # Initial condition
time = np.linspace(0, 10, 100)  # Time array

# Initialize past values container
past_values = PastValues()

# Solve ODE
ETA = odeint(eta_func, init_cond, time, args=(past_values, theta, gamma, beta, zeta, tau))

# Access components
eta0 = ETA[:, 0]
print(eta0)
