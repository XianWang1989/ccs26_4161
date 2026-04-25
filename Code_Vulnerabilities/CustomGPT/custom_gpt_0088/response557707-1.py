
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Access dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Mask the invalid values
invalid_value = 9.969209968386869e+36
masked_precip = np.ma.masked_equal(precip, invalid_value)

for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(masked_precip[i])
