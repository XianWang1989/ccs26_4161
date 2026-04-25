
import numpy as np
from scipy.integrate import odeint

# Parameters
a = 1
b = 5
tau = 3

# Initialize history
history_length = 100  # Length of history to store past values
past_eta = np.zeros((history_length,))
time_steps = np.linspace(0, 20, 200)

# Define the differential equation function
def etaFunc(eta, t):
    # Update the history array
    idx = int(t) % history_length  # Simple index for history (modular)
    past_eta[idx] = eta  # Store current eta

    # Compute past values with the phase shift
    shifted_idx = (int(t - tau) % history_length) if (t - tau) >= 0 else idx
    eta_past = past_eta[shifted_idx]

    # Return the change in eta
    d_eta = a * eta + b * eta_past
    return d_eta

# Initial condition
initCond = 1.0

# Perform the integration
ETA = odeint(etaFunc, initCond, time_steps)

# Extract individual components if needed
eta_0 = ETA[:, 0]

# Display the results (optional)
import matplotlib.pyplot as plt

plt.plot(time_steps, eta_0, label='eta(t)')
plt.xlabel('Time')
plt.ylabel('eta')
plt.title('Response of eta over time')
plt.legend()
plt.show()
