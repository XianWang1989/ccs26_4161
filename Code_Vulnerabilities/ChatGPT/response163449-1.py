
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3  # Time delay

# Define the number of past values you want to store (depends on your system)
num_past_values = int(tau + 1)  # Change as needed

# Create a class to handle the delayed states
class StateBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = np.zeros((size,))
        self.index = 0

    def update(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.size  # Wrap around to overwrite old values

    def get_past(self, delay):
        idx = (self.index - int(delay)) % self.size  # Get index for past value
        return self.buffer[idx]

# Initialize the state buffer
state_buffer = StateBuffer(num_past_values)

# Define the differential equation system with time delay
def etaFunc(A, t):
    state_buffer.update(A)  # Update the buffer with current value

    # Retrieve past values if needed
    past_value = state_buffer.get_past(tau)  # Get the delayed value
    dA_dt = a * A + b * past_value  # Define the differential equation
    return dA_dt

# Time range for the simulation
time = np.linspace(0, 20, 200)  # From 0 to 20 with 200 points

# Initial conditions
initCond = [0]  # You can start with any initial value

# Solve the ODE
ETA = odeint(etaFunc, initCond, time)

# Access components of ETA
eta_0 = ETA[:, 0]

# Plotting (optional)
import matplotlib.pyplot as plt

plt.plot(time, eta_0, label='eta_0')
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('Response with Time Delay')
plt.legend()
plt.grid()
plt.show()
