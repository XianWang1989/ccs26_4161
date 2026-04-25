
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3  # Time delay
time_delay_steps = 10  # How many previous steps to save for interpolation

# Define the system of equations
class PastValues:
    def __init__(self):
        self.history = []

    def record(self, value):
        self.history.append(value)
        if len(self.history) > time_delay_steps:
            self.history.pop(0)

    def get_past_value(self, t, time, dt):
        index = np.searchsorted(time, t)
        if index > 0:
            return self.history[index - 1]
        return 0  # If no past value is available

def eqtnSystem(Y, t, past_eta, time, dt):
    # Record current value
    past_eta.record(Y)

    Y_tau = past_eta.get_past_value(t - tau, time, dt)  # Get Y(t - tau)
    dYdt = a * Y + b * Y_tau  # Your equation
    return dYdt

# Time vector
t = np.linspace(0, 50, 500)
dt = t[1] - t[0]  # Time step

# Initial conditions
initCond = [0]  # Starting value for Y

# Create a PastValues instance to manage past values
past_eta = PastValues()

# Integrate the ODE
ETA = odeint(eqtnSystem, initCond, t, args=(past_eta, t, dt))

# Results
y_values = ETA[:, 0]
import matplotlib.pyplot as plt

plt.plot(t, y_values, label='Y(t)')
plt.xlabel('Time')
plt.ylabel('Y')
plt.legend()
plt.title('ODE Solution with Time Delay')
plt.grid()
plt.show()
