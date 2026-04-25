
import numpy as np
from scipy.integrate import odeint

# Define constants
a = 1
b = 5
tau = 3  # delay in time

# Initialize past values storage
max_timesteps = 1000
history = np.zeros((max_timesteps, 5))  # Assuming eta has 5 components
current_index = 0

def etaFunc(A, t):
    global current_index
    # Access past values based on the variable 'tau'
    past_index = current_index - int(tau) if current_index - int(tau) >= 0 else current_index

    # Calculate the current derivatives
    dA_dt = np.zeros_like(A)
    dA_dt[0] = a * A[0] + b * history[past_index, 0]
    dA_dt[1] = (gamma[1,1] * xi(t - theta[1])[1] - A[1] + zeta[1]) / tau
    # Additional equations here...

    return dA_dt

# Time settings
time = np.linspace(0, 100, max_timesteps)

# Initial condition
initCond = np.zeros(5)

# Integration process
for i in range(max_timesteps):
    if i > 0:
        history[i] = history[i-1] + etaFunc(history[i-1], time[i-1]) * (time[i] - time[i-1])
    else:
        history[i] = initCond

current_index = i  # Update the current index 

# Now you can get the results
ETA = history[:current_index + 1]
