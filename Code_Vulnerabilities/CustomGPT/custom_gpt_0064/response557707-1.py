
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='netCDF4')

# Get the dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define a mask for the invalid value
invalid_value = 9.969209968386869e+36

# Loop through time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Get precipitation for the current time step
    current_precip = precip[i, :, :]  # Assuming precip has time as the first dimension

    # Mask the invalid values
    valid_precip = np.where(current_precip == invalid_value, np.nan, current_precip)

    # Print the valid precipitation values
    print(valid_precip)
