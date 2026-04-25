
import numpy as np
from scipy.integrate import odeint

class PhaseShiftedODE:
    def __init__(self, tau):
        self.tau = tau
        self.history = []

    def eqtnSystem(self, A, t):
        if len(self.history) > 0:
            Y_past = self.history[-1] if t - self.tau < 0 else self.get_past_value(t)
        else:
            Y_past = 0

        a = 1
        b = 5
        return a * A + b * Y_past

    def get_past_value(self, t):
        for time, value in reversed(self.history):
            if time <= t - self.tau:
                return value
        return 0

    def store_value(self, t, value):
        self.history.append((t, value))

def model(A, t, ode_model):
    dYdt = ode_model.eqtnSystem(A, t)
    ode_model.store_value(t, A)
    return dYdt

# Setup parameters
tau = 3
initCond = [0]  # Initial condition
time = np.linspace(0, 10, 100)

# Create the ODE model
ode_model = PhaseShiftedODE(tau)

# Solve the ODE
ETA = odeint(model, initCond, time, args=(ode_model,))

# Access results
eta_0 = ETA[:, 0]

print(eta_0)
