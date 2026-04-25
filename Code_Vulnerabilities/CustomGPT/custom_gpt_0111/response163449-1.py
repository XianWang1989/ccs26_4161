
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d

# Parameters
a = 1
b = 5
tau = 3
time = np.linspace(0, 30, 300)  # Time array
initCond = [0]  # Initial condition for Y

def etaFunc(Y, t, past_values):
    # Interpolating past values based on time
    if t - tau < 0:
        Y_tau = 0  # No past value if time is not enough
    else:
        Y_tau = past_values(t - tau)  # Get past value from interpolation

    dYdt = a * Y + b * Y_tau
    return [dYdt]

# Store results for interpolation
results = []
for t in time:
    results.append(initCond[0] if len(results) == 0 else results[-1][0])  # Append current value

# Perform integration
ETA = odeint(etaFunc, initCond, time, args=(interp1d(time, results, fill_value='extrapolate', bounds_error=False),))
# Update results for future time points
results.extend(ETA[:, 0])

# Example retrieve
eta_0 = ETA[:, 0]

# Plotting or further processing could be done here
