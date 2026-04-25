
import netCDF4
import numpy as np

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Correct array type

# Iterate over time and print the corresponding precipitation data
for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(precip[i])  # Access precipitation data for each time index

f.close()  # Close the netCDF file
