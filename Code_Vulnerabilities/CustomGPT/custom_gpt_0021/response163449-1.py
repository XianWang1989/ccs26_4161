
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Time parameters
start_time = 0
end_time = 20
time = np.linspace(start_time, end_time, 100)

# Define the system of equations
def etaFunc(A, t, past_values, tau):
    # Unpack the array of variables
    eta0, eta1, eta2, eta3, eta4 = A

    # Define constants (example values)
    gamma = np.array([[1, 0], [0, 1], [1, 0]])
    beta = np.array([[1, 1, 1], [1, 1], [1]])
    zeta = np.array([0, 0, 0, 0, 0])
    tau_values = np.array([1, 1, 1, 1, 1])  # Example tau values
    theta = np.array([1, 2, 3, 4, 5])

    # Ensure past values are within the time range
    if t - tau < start_time:
        past_eta3 = past_values[int(0)]  # Default if too early
        past_eta4 = past_values[int(0)]  # Default if too early
    else:
        idx = np.searchsorted(time, t - tau) - 1
        past_eta3 = past_values[idx][3]
        past_eta4 = past_values[idx][4]

    # Define the derivatives using the current and past values
    dEta0_dt = (gamma[0, 0] * eta0 - eta0 + zeta[0]) / tau_values[0]
    dEta1_dt = (gamma[1, 1] * eta1 - eta1 + zeta[1]) / tau_values[1]
    dEta2_dt = (gamma[2, 2] * eta2 - eta2 + zeta[2]) / tau_values[2]
    dEta3_dt = (beta[3, 0] * past_eta3 + beta[3, 1] * past_eta4 - eta3 + zeta[3]) / tau_values[3]
    dEta4_dt = (beta[4, 3] * past_eta3 - eta4 + zeta[4]) / tau_values[4]

    return [dEta0_dt, dEta1_dt, dEta2_dt, dEta3_dt, dEta4_dt]

# Initial conditions
initCond = [1, 0, 0, 0, 0]

# Store results for interpolation
results = []

# Function to integrate and store results
for t in time:
    if len(results) > 0:
        past_values = np.array(results)
    else:
        past_values = np.array([initCond])

    next_result = odeint(etaFunc, initCond, [t], args=(past_values, 3))[0]

    results.append(next_result)

results = np.array(results)

# Access individual components
eta0 = results[:, 0]
eta1 = results[:, 1]
eta2 = results[:, 2]
eta3 = results[:, 3]
eta4 = results[:, 4]

# Now you can plot or analyze the results
import matplotlib.pyplot as plt

plt.plot(time, eta0, label='eta0')
plt.plot(time, eta1, label='eta1')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Differential Equations with Phase Shift')
plt.show()
