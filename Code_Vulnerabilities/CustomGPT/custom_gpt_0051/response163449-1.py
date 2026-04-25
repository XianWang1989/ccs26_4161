
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Store past eta values
class EtaMemory:
    def __init__(self):
        self.eta_history = []
        self.time_history = []

    def update(self, t, eta):
        self.eta_history.append(eta)
        self.time_history.append(t)

    def get_past_value(self, past_time):
        # Find the index of the nearest time point less than `past_time`
        index = np.searchsorted(self.time_history, past_time) - 1
        if index < 0:
            return 0  # or some default value
        return self.eta_history[index]

# Define the differential equations
def etaFunc(eta, t, mem):
    # Your constants
    a = 1
    b = 5
    tau = 3

    # Update memory with current eta and time
    mem.update(t, eta)

    # Calculate the current derivatives
    Y = eta
    Y_past = mem.get_past_value(t - tau)

    return a * Y + b * Y_past

# Initial conditions and time vector
initCond = np.array([0.5])  # Example initial condition
time = np.linspace(0, 20, 100)  # Time span

# Create an instance of EtaMemory
mem = EtaMemory()

# Use odeint to solve the system
ETA = odeint(etaFunc, initCond, time, args=(mem,))

# Plot the results
plt.plot(time, ETA)
plt.xlabel('Time')
plt.ylabel('ETA')
plt.title('Solution of Differential Equation with Phase Shift')
plt.show()
