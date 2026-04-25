
import numpy as np
from scipy import integrate

class DelayODE:
    def __init__(self, tau):
        self.tau = tau
        self.history = []

    def past_eta(self, t):
        if not self.history:
            return 0  # Or some default value
        # Find the closest past value with time shifted by tau
        for (time, value) in reversed(self.history):
            if time <= t:
                return value
        return 0  # Or some default value

    def eta_func(self, A, t):
        # Append current state to the history
        self.history.append((t, A))

        # Clean up history by removing old entries
        self.history = [(time, value) for time, value in self.history if t - time <= self.tau]

        # Constants
        a = 1
        b = 5

        # Calculate derivatives with the past value
        dYdt = np.zeros_like(A)
        dYdt[0] = a * A[0] + b * self.past_eta(t - self.tau)
        # Continue similarly for other components (dYdt[1], dYdt[2], etc.)
        # Implement your other equations similarly here...

        return dYdt

# Example initialization
tau = 3
delay_ode = DelayODE(tau)
init_cond = np.array([1.0])  # Set initial conditions as needed
time = np.linspace(0, 10, 100)  # Time array

# Using odeint to solve the ODE
ETA = integrate.odeint(delay_ode.eta_func, init_cond, time)

# Accessing the individual components
eta_0 = ETA[:, 0]
