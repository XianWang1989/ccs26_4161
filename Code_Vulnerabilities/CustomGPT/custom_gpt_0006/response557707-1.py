
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Dimensions and variables of the NetCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming 9.969209968386869e+36 is the fill value
fill_value = 9.969209968386869e+36

# Loop through time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    valid_precip = precip[i][precip[i] != fill_value]  # Filter out fill values
    print(valid_precip)
