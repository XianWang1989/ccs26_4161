
import numpy as np
from scipy import integrate

# Global variable to store past values of eta
past_values = []

def pastEta(t_value):
    # Retrieving past values based on the provided time value
    # Assume time_values is a list of time points where the corresponding eta values were computed:
    time_values = np.array([t[0] for t in past_values])
    index = np.searchsorted(time_values, t_value) - 1  # Find the index of the last time less than t_value
    if index >= 0:
        return past_values[index][1]  # Return the corresponding eta value
    else:
        return np.zeros(eta_shape)  # Return a zero state if no past value is found

def etaFunc(A, t):
    global past_values
    # ... definition of all those constants is here ...

    # Store the current state with the current time
    past_values.append((t, A))

    new_eta = np.array([
        (gamma[0,0] * xi(t - theta[0])[0] - eta[0] + zeta[0]) / tau[0],
        (gamma[1,1] * xi(t - theta[1])[1] - eta[1] + zeta[1]) / tau[1],
        (gamma[2,2] * xi(t - theta[2])[2] - eta[2] + zeta[2]) / tau[2],
        (beta[3,0] * pastEta(t - theta[3])[0] + 
         beta[3,1] * pastEta(t - theta[4])[1] + 
         beta[3,2] * pastEta(t - theta[5])[2] - eta[3] + zeta[3]) / tau[3],
        (beta[4,3] * pastEta(t - theta[6])[3] + 
         beta[4,2] * pastEta(t - theta[7])[2] - eta[4] + zeta[4]) / tau[4]
    ])

    return new_eta

# Example of initial condition and defining time points
initCond = np.zeros(5)  # Adjust based on your system's needs
time = np.linspace(0, 10, 100)  # Time array for integration

# Running the odeint function
ETA = integrate.odeint(etaFunc, initCond, time)

# Accessing individual components
eta_0 = ETA[:, 0]

# Note: Ensure to clear the past_values list between different simulation runs if needed
