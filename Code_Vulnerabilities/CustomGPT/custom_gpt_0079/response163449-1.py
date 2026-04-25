
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Define the system of equations
def etaFunc(A, t, history):
    # Unpack the state vector
    eta_0, eta_1, eta_2, eta_3, eta_4 = A
    # Constants
    gamma = np.array([[1, 0], [0, 1], [1, 0]])
    zeta = np.zeros(5)
    beta = np.random.rand(5, 5)
    tau = [1, 2, 3, 3, 3]  # Example tau values
    theta = [2, 2, 2, 2, 2]

    # History interpolation
    t_history = np.arange(len(history))
    interp_eta = interp1d(t_history, history, axis=0, fill_value="extrapolate")

    past_eta_3 = interp_eta(t - theta[3]) if t - theta[3] >= 0 else np.zeros(5)
    past_eta_4 = interp_eta(t - theta[4]) if t - theta[4] >= 0 else np.zeros(5)

    # Define the equations
    return np.array([
        (gamma[0, 0] * 0 - eta_0 + zeta[0]) / tau[0],
        (gamma[1, 1] * 0 - eta_1 + zeta[1]) / tau[1],
        (gamma[2, 2] * 0 - eta_2 + zeta[2]) / tau[2],
        (beta[3, 0] * past_eta_3[0] + beta[3, 1] * past_eta_4[1] - eta_3 + zeta[3]) / tau[3],
        (beta[4, 3] * past_eta_4[3] - eta_4 + zeta[4]) / tau[4],
    ])

# Initial conditions
initCond = [0, 0, 0, 0, 0]
time = np.linspace(0, 10, 100)

# To store history of eta
history = np.zeros((len(time), 5))

# Solve the ODE
for i, t_val in enumerate(time):
    if i == 0:
        history[i] = initCond
    else:
        history[i] = odeint(etaFunc, history[i-1], [time[i-1], t_val], args=(history,))[-1]

# Now you can access eta values
eta_0 = history[:, 0]
eta_1 = history[:, 1]

# Output the results
print("eta_0:", eta_0)
print("eta_1:", eta_1)
