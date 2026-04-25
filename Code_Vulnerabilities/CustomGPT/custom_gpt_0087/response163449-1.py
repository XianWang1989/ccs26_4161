
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3.0
time = np.linspace(0, 10, 100)

# Define the system with a history array
def etaFunc(Y, t, history):
    # Use the history array to get past values
    if t < tau:
        Ytau = 0  # Default value if not enough history
    else:
        Ytau = history[int((t - tau) / (time[1] - time[0]))]  # Get past value

    dYdt = a * Y + b * Ytau
    history.append(Y)  # Update history
    return dYdt

# Initial condition
initCond = [0]

# Store history for past values
history = []

# Run the integration
ETA = odeint(etaFunc, initCond, time, args=(history,))

# Access individual components
eta_0 = ETA[:, 0]

# Display the result
import matplotlib.pyplot as plt

plt.plot(time, eta_0)
plt.xlabel('Time')
plt.ylabel('eta_0')
plt.title('eta_0 over Time')
plt.show()
