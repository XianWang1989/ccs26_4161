
import numpy as np
from scipy.integrate import odeint

# Define the time delay and history length
tau = 3
history_length = 100  # Adjust as needed for your simulation duration

# Function to store past values of eta
class PastValues:
    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.append(value)
        if len(self.values) > history_length:
            self.values.pop(0)  # Keep only the most recent values

    def get(self, t, current_time):
        time_index = int(current_time - t)
        if 0 <= time_index < len(self.values):
            return self.values[time_index]
        else:
            return 0  # Return 0 or a suitable default if out of bounds

# Create an instance to store past values
past = PastValues()

# Define the differential equations system
def etaFunc(A, t):
    # Define constants
    gamma = [[1, 0], [0, 1], [1, 1]]  # Example constants
    beta = [[1, 2], [2, 1], [1, 1], [1, 0]]
    zeta = [1, 1, 1, 1, 1]
    theta = [1, 2, 3, 4, 5]

    # Store the current state
    current_eta = A.copy()
    past.add(current_eta)  # Update history

    # Now calculate the derivatives
    dA_dt = np.array([
        (gamma[0][0] * current_eta[0] - current_eta[0] + zeta[0]) / 1,
        (gamma[1][1] * current_eta[1] - current_eta[1] + zeta[1]) / 1,
        (gamma[2][2] * current_eta[2] - current_eta[2] + zeta[2]) / 1,
        (beta[3][0] * past.get(t - theta[3], t) +
         beta[3][1] * past.get(t - theta[4], t) - current_eta[3] + zeta[3]) / 1,
        (beta[4][3] * past.get(t - theta[6], t) +
         beta[4][2] * past.get(t - theta[7], t) - current_eta[4] + zeta[4]) / 1
    ])

    return dA_dt

# Initialize conditions and time array
initCond = [0, 0, 0, 0, 0]
time = np.linspace(0, 20, 200)

# Solve the ODE
ETA = odeint(etaFunc, initCond, time)

# Extract variables as needed
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]

# Now you can plot or further analyze your results as needed
