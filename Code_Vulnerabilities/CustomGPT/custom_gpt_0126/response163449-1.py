
import numpy as np
from scipy.integrate import odeint

# Define a class to manage the history of past values
class PastValues:
    def __init__(self, size):
        self.size = size
        self.values = []

    def add(self, value):
        if len(self.values) >= self.size:
            self.values.pop(0)
        self.values.append(value)

    def get(self, time_index):
        if time_index < len(self.values):
            return self.values[time_index]
        else:
            return 0  # Return 0 or some default value if there's no past value

# Initialize past values storage
past_values = PastValues(size=10)  # adjust size as needed

def etaFunc(A, t):
    global past_values
    # Example constants
    gamma = np.array([[1.0], [1.0], [1.0], [1.0], [1.0]])
    zeta = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    tau = 3

    # Calculate new values
    new_eta = np.array([(gamma[0,0] * A[0] - A[0] + zeta[0]) / tau,
                        (gamma[1,1] * A[1] - A[1] + zeta[1]) / tau,
                        (gamma[2,2] * A[2] - A[2] + zeta[2]) / tau,
                        (0.5 * past_values.get(-2) - A[3] + zeta[3]) / tau,  # Past value for eta_3
                        (0.5 * past_values.get(-1) - A[4] + zeta[4]) / tau])  # Past value for eta_4

    # Store current values in past values
    past_values.add(A[3])  # Assuming A[3] corresponds to eta_3

    return new_eta

# Initial conditions and time settings
initCond = [1, 2, 3, 4, 5]
time = np.linspace(0, 10, 100)

# Integrate the system
ETA = odeint(etaFunc, initCond, time)

# Access individual components
eta_0 = ETA[:, 0]
eta_1 = ETA[:, 1]
# etc.
