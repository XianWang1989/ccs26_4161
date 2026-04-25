import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Parameters
a = 1
b = 5
tau = 3

# Define initial history (only for t <= 0)
def history(t):
    return np.sin(t)  # example initial history function

# Create a class to manage the delayed system state
class DelayedSystem:
    def __init__(self):
        self.solution = None
        self.t_values = None

    def rhs(self, Y, t):
        if t - tau < 0:
            Y_tau = history(t - tau)
        else:
            Y_tau = self.interpolator(t - tau)
        return a * Y + b * Y_tau

    def integrate(self, Y0, t_values):
        self.t_values = t_values
        self.solution = []
        for i, t in enumerate(t_values):
            if i == 0:
                Y = Y0
            else:
                # Create interpolator from previously calculated points
                past_times = t_values[:i]
                past_ys = np.array(self.solution)
                self.interpolator = interp1d(past_times, past_ys.flatten(), fill_value="extrapolate")
                Y = odeint(self.rhs, Y, [t_values[i-1], t_values[i]])[1]
            self.solution.append(Y)
        return np.array(self.solution).reshape(-1)

# Initialize and solve
sys = DelayedSystem()
t_vals = np.linspace(0, 20, 500)
Y0 = [history(0)]  # initial condition at t=0
Y_vals = sys.integrate(Y0, t_vals)

# Plot
plt.plot(t_vals, Y_vals)
plt.title("Solution of DDE using interpolation workaround")
plt.xlabel("Time t")
plt.ylabel("Y(t)")
plt.grid(True)
plt.show()
