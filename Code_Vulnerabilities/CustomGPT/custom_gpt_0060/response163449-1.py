
import numpy as np
from scipy.integrate import odeint

class StateHistory:
    def __init__(self, init_cond, max_delay):
        self.values = [init_cond]  # Store initial condition
        self.max_delay = max_delay   # Time delay to consider

    def get_value(self, t):
        """ Returns the value at a given time t based on stored history. """
        if t < len(self.values):
            return self.values[int(t)]  # Assuming t is an integer time index
        else:
            return self.values[-1]  # Return the last known state if out of bounds

    def update(self, new_value):
        """ Store the new computed value for the current time step. """
        self.values.append(new_value)
        # Maintain the history size based only on the maximum delay
        if len(self.values) > self.max_delay:
            self.values.pop(0)

def etaFunc(A, t, history, tau, beta, theta, gamma, zeta):
    # Example constants, update based on your model specifics
    a = 1.0
    b = 5.0

    # Get past values using the history class
    past_eta0 = history.get_value(t-theta[0]) if t-theta[0] >= 0 else 0
    past_eta1 = history.get_value(t-theta[1]) if t-theta[1] >= 0 else 0
    past_eta2 = history.get_value(t-theta[2]) if t-theta[2] >= 0 else 0

    # Define the differential equations based on your system
    dEta_dt = np.array([
        (gamma[0][0] * A[0] - A[0] + zeta[0]) / tau[0],
        (gamma[1][1] * A[1] - A[1] + zeta[1]) / tau[1],
        (gamma[2][2] * A[2] - A[2] + zeta[2]) / tau[2],
        (beta[3][0] * past_eta0 + beta[3][1] * past_eta1 + beta[3][2] * past_eta2 - A[3] + zeta[3]) / tau[3],
        (beta[4][3] * past_eta0 + beta[4][2] * past_eta1 - A[4] + zeta[4]) / tau[4]
    ])

    return dEta_dt

# Constants and parameters
initCond = [0, 0, 0, 0, 0]  # Initial conditions for eta components
tau = [1, 1, 1, 1, 1]  # Time constants
beta = np.zeros((5, 5))  # Example coefficient matrix
theta = [1, 2, 3, 1, 2]  # Time delays
gamma = np.eye(5)  # Identity matrix for simplicity
zeta = [0, 0, 0, 0, 0]  # External influences

# Create a history management object
max_delay = max(theta)
history = StateHistory(initCond, max_delay)

# Time vector for integration
time = np.linspace(0, 10, 100)  # From 0 to 10, with 100 steps

# A function to wrap the call to etaFunc, to use with odeint
def wrapped_etaFunc(A, t):
    # Update the state history
    history.update(A)
    return etaFunc(A, t, history, tau, beta, theta, gamma, zeta)

# Run the integration
ETA = odeint(wrapped_etaFunc, initCond, time)

# Now you can access individual components of ETA
print(ETA[:, 0])  # Access eta_0
print(ETA[:, 1])  # Access eta_1
print(ETA[:, 2])  # Access eta_2
print(ETA[:, 3])  # Access eta_3
print(ETA[:, 4])  # Access eta_4
