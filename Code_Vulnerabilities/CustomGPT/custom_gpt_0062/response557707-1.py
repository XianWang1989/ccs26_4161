
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Access dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Remove dtype restriction

# Loop through the time variable to extract precipitation
for t_index in range(len(time)):
    # Get precipitation for the current time index
    precip_values = precip[t_index, :, :]  # Adjust based on the shape of your data

    # Check for the placeholder value and only print valid values
    if np.any(precip_values != 9.969209968386869e+36):  # Masked values
        print("Precipitation for time index:", t_index)
        print(precip_values[precip_values != 9.969209968386869e+36])

# Close the netCDF file
f.close()
