
def etaFunc(eta, t, time_points):
    # Define your constants here, adjust as needed.
    gamma = np.array([[1]])  # Placeholder
    zeta = np.array([1])      # Placeholder
    tau = 3                    # Time delay
    beta = np.array([[1]])     # Placeholder
    theta = [1, 1, 1, 1, 1, 1] # Placeholder for theta parameters

    # Interpolate past values of eta
    if t - theta[0] >= 0:
        past_eta_func = interp1d(time_points, eta_history, fill_value="extrapolate")
        eta_past = past_eta_func(t - theta[0])
    else:
        eta_past = 0 # Default value if t - theta[0] is out of range

    # Define the system of equations
    dEta_dt = np.zeros_like(eta)
    dEta_dt[0] = (gamma[0,0] * eta[0] - eta[0] + zeta[0]) / tau
    dEta_dt[1] = (gamma[1,1] * eta[1] - eta[1] + zeta[1]) / tau
    dEta_dt[2] = (gamma[2,2] * eta[2] - eta[2] + zeta[2]) / tau
    dEta_dt[3] = (beta[3,0] * eta_past - eta[3] + zeta[3]) / tau
    # Additional components can be defined similarly as needed

    return dEta_dt
