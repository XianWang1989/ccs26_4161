
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Iterate through each time index
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extract the precipitation for the current time step
    current_precip = precip[i, :, :]  # Adjust based on the shape of your data
    print(current_precip)

# Don't forget to close the dataset
f.close()
