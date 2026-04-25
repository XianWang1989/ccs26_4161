import arcpy
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Precipitation values

# Mask out the invalid value (9.969209968386869e+36)
invalid_value = 9.969209968386869e+36
precip_masked = np.ma.masked_equal(precip, invalid_value)

# Iterate through the time dimension
for i in time:
    print("Precipitation for year:", i)
    
    # Print the masked precipitation for the current time step
    print(precip_masked[i, :, :])
