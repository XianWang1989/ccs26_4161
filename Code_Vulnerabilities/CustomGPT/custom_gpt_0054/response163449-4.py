
# Loop through time to integrate and store results
for i, t in enumerate(time):
    if i > 0:
        eta = odeint(etaFunc, initCond, [time[i-1], time[i]], args=(time,))[-1]
        eta_history.append(eta)

eta_history = np.array(eta_history)
