
masked_precip = np.ma.masked_where(precip == 9.969209968386869e+36, precip)

for i in range(len(time)):
    print("Precipitation for:", time[i])
    print(masked_precip[i])  # Will not show masked values
