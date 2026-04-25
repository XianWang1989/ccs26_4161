
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function that remembers past values
class PastValues:
    def __init__(self, tau, max_len):
        self.tau = tau
        self.max_len = max_len
        self.values = []

    def add(self, value):
        if len(self.values) >= self.max_len:
            self.values.pop(0)  # keep the array within max_len
        self.values.append(value)

    def get(self, current_t, target_t):
        index = int(target_t // self.tau)  # calculate the index of the past value
        if index >= len(self.values) or index < 0:
            return 0  # or any default value you deem appropriate
        return self.values[index]

# Define your differential equations system
def etaFunc(Y, t, past):
    a = 1
    b = 5
    tau = 3

    # Add the current value to the past values
    past.add(Y[0])

    # Get values from past
    Y_past = past.get(t, t-tau)

    dYdt = a * Y[0] + b * Y_past
    return [dYdt]

# Initial conditions
initCond = [1]  # Initial value of Y(0)
time = np.linspace(0, 30, 300)  # Time from 0 to 30 in 300 points

# Create an instance to keep track of past values
past_values = PastValues(tau=3, max_len=len(time))

# Integrate the system using odeint
ETA = odeint(etaFunc, initCond, time, args=(past_values,))

# Plot the result
plt.plot(time, ETA[:, 0], label='Y(t)')
plt.title('Differential Equation with Phase Shift')
plt.xlabel('Time')
plt.ylabel('Y(t)')
plt.legend()
plt.show()
