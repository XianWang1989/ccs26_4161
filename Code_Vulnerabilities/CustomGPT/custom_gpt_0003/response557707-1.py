
import arcpy
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Note: No need for dtype here unless required

# Assuming 'time' is the first dimension and 'precip' has the shape (time, lat, lon)
for i in range(len(time)):  # Iterate over the time indices
    print("Precipitation for:", time[i])
    print(precip[i])  # Extract the precipitation for the specific time index
