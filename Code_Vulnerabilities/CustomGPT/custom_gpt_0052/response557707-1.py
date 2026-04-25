
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Obtain precipitation data

# Loop through the time index
for i in range(len(time)):
    print(f"Precipitation for year index {i}: {time[i]}")
    print(precip[i, :, :])  # Access precipitation for the specific time index

# Close the netCDF file
f.close()
