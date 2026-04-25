
# Define your fill value (example)
fill_value = 9.969209968386869e+36

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for index", i, ":", time[i])

    current_precip = precip[i, :, :]

    # Remove fill values
    current_precip[current_precip == fill_value] = np.nan  # or any other placeholder

    print(current_precip)
