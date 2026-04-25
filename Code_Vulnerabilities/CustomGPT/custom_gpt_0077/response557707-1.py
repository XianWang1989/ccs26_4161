
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract the dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' is the correct variable name

# Loop through time indices and extract precipitation data for each time step
for i in range(len(time)):
    print("Precipitation for:", time[i])
    print(precip[i])  # Accessing precipitation data for the current time index

# Close the dataset
f.close()
