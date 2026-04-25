
import numpy as np
from scipy.integrate import odeint

class History:
    def __init__(self, tau):
        self.tau = tau
        self.past_values = []

    def update(self, new_value, current_time, current_time_step):
        # Store the new value with its timestamp
        self.past_values.append((current_time, new_value))
        # Remove entries older than t - tau
        self.past_values = [(t, val) for t, val in self.past_values if t > current_time - self.tau]

    def get_past_value(self, current_time):
        # Find the most recent value within the time shift
        for t, val in reversed(self.past_values):
            if t <= current_time:
                return val
        return 0  # Return 0 if no past value is found

def etaFunc(A, t, history):
    gamma = np.array([[1, 0], [0, 1], [1, 1]])
    zeta = np.zeros(4)  # Example values
    tau = [1, 1, 1, 1]  # Example tau values
    theta = [3, 3, 3, 3]  # Example time shifts

    # Calculate current eta based on past values
    past_eta_3 = history.get_past_value(t - theta[3])
    past_eta_4 = history.get_past_value(t - theta[4])

    # Example differential equations
    d_eta = [
        (gamma[0, 0] * A[0] - A[0] + zeta[0]) / tau[0],
        (gamma[1, 1] * A[1] - A[1] + zeta[1]) / tau[1],
        (gamma[2, 2] * A[2] - A[2] + zeta[2]) / tau[2],
        (beta[3, 0] * past_eta_3 + beta[3, 1] * past_eta_4 - A[3] + zeta[3]) / tau[3],
        (beta[4, 3] * past_eta_3 + beta[4, 2] * past_eta_4 - A[4] + zeta[4]) / tau[4],
    ]

    return d_eta

# Parameters
beta = np.random.rand(5, 5)  # Example beta matrix
init_cond = [1, 1, 1, 1, 1]  # Initial conditions
time = np.linspace(0, 10, 100)  # Time points

# Create history object
history = History(tau=3)

# Store results for integration
result = []

def wrapper_odeint(A, t):
    # Update history
    history.update(A, t, None)
    return etaFunc(A, t, history)

ETA = odeint(wrapper_odeint, init_cond, time)

# Access individual components
eta0 = ETA[:, 0]
eta1 = ETA[:, 1]
