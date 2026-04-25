
import numpy as np
from scipy.integrate import odeint

class History:
    def __init__(self, max_time):
        self.max_time = max_time
        self.values = []

    def add(self, t, value):
        self.values.append((t, value))
        # Keep only values within the time window of interest
        self.values = [(time, val) for time, val in self.values if time > t - self.max_time]

    def get(self, t):
        # Find the closest previous value to t
        for time, val in reversed(self.values):
            if time <= t:
                return val
        return 0  # Default if no past value exists

def etaFunc(A, t, history):
    a = 1
    b = 5
    tau = 3

    # You can get the past value using the history object
    Y_past = history.get(t - tau)

    # Update the history with the current time and current value of A
    history.add(t, A)

    # Return the derivatives
    return (a * A + b * Y_past,)

# Initialize parameters
init_cond = [0]  # Initial condition
time = np.linspace(0, 10, 100)  # Time points
history = History(max_time=tau)  # Create a history object

# Integrate
ETA = odeint(etaFunc, init_cond, time, args=(history,))

# Print results for verification
print(ETA[:, 0])
