
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract variables
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
time = f.variables['time'][:]
precip = f.variables['pre'][:]

# Loop through time and print precipitation values for each year
for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(precip[i, :, :])  # Adjust indexing to access the correct precip data
