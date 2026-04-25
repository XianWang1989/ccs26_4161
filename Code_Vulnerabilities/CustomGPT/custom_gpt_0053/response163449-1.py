
import numpy as np
from scipy.integrate import odeint

# Constants
a = 1
b = 5
tau = 3

# Function to calculate eta
def etaFunc(A, t, history):
    # Store current value to history
    history.append(A.copy())

    # Calculate past values within the history
    # Interpolating to find Y(t-tau)
    if len(history) > tau:
        Y_past = history[-tau]  # A[t-tau] corresponds to history[-tau]
    else:
        Y_past = A  # Use current value if insufficient history

    # Define the system of equations
    dA_dt = a * A + b * Y_past
    return dA_dt

# Function to run the integration with history tracking
def run_integration(init_cond, t):
    history = []
    # Solve ODE with a lambda to allow for history passing
    ETA = odeint(lambda A, t: etaFunc(A, t, history), init_cond, t)
    return ETA, history

# Initial conditions and time
initCond = [0]  # Starting conditions
time = np.linspace(0, 30, 100)  # Time array

ETA, history = run_integration(initCond, time)

# Now you can access individual eta components
eta_0 = ETA[:, 0]
