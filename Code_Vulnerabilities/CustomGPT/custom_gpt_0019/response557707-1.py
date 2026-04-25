
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjust according to actual variable name

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(precip[i, :, :])  # Use proper indexing for 3D data (time, lat, lon)

# Close the netCDF file
f.close()
