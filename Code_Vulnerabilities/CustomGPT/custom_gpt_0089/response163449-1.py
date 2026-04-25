
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
gamma = np.array([[1], [1], [1]])
beta = np.zeros((5, 5))  # Replace with your values
zeta = np.array([0, 0, 0, 0, 0])
tau = np.array([1, 1, 1, 1, 1])  # Replace with your values
theta = np.array([3, 3, 3, 3, 3])  # Phase shifts

# Initial Conditions
initCond = [0, 0, 0, 0, 0]  # Starting values for eta
time = np.linspace(0, 20, 100)  # Time array
past_values = []  # To store past eta values

def pastEta(t, past_values):
    # Interpolate past values based on time
    if len(past_values) == 0 or t <= 0:
        return np.zeros(3)  # Default if no past values exist
    idx = max(0, np.searchsorted(past_values[:, 0], t) - 1)
    return past_values[idx, 1:]

def etaFunc(A, t):
    global past_values
    # Store current time and state
    past_values.append((t, A.copy()))

    results = np.zeros(5)
    results[0:3] = (gamma[0, 0] * xi(t - theta[0])[0] - A[0] + zeta[0]) / tau[0],\
                    (gamma[1, 1] * xi(t - theta[1])[1] - A[1] + zeta[1]) / tau[1],\
                    (gamma[2, 2] * xi(t - theta[2])[2] - A[2] + zeta[2]) / tau[2])

    # Handle past eta values
    if t >= theta[3]:
        past_eta_values = pastEta(t - theta[3], past_values)
        results[3] = (beta[3, 0] * past_eta_values[0] + 
                      beta[3, 1] * past_eta_values[1] + 
                      beta[3, 2] * past_eta_values[2] - A[3] + zeta[3]) / tau[3]

    if t >= theta[4]:
        past_eta_values = pastEta(t - theta[6], past_values)
        results[4] = (beta[4, 3] * past_eta_values[3] + 
                      beta[4, 2] * past_eta_values[2] - A[4] + zeta[4]) / tau[4]

    return results

# Function to compute xi (example)
def xi(t):
    # Example implementation, replace with actual logic
    return np.array([np.sin(t), np.cos(t), np.sin(t)])

# Integrate using odeint
ETA = odeint(etaFunc, initCond, time)

# Plotting the results
plt.plot(time, ETA[:, 0], label='eta_0')
plt.plot(time, ETA[:, 1], label='eta_1')
plt.plot(time, ETA[:, 2], label='eta_2')
plt.plot(time, ETA[:, 3], label='eta_3')
plt.plot(time, ETA[:, 4], label='eta_4')
plt.legend()
plt.xlabel('Time')
plt.ylabel('ETA Values')
plt.title('ETA over Time with Phase Shift')
plt.show()
