
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Read entire precipitation data

# Loop through time and extract precipitation for each time step
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Ensure you get the corresponding precipitation values for the time index i
    precip_values = precip[i, :, :]  # Assuming precip has time as the first dimension
    print(precip_values)
