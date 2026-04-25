
import numpy as np
import netCDF4 as nc

# Open netCDF file
f = nc.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming the missing value is set as 9.969209968386869e+36, replace it with NaN
missing_value = 9.969209968386869e+36
precip[precip == missing_value] = np.nan

# Loop through each time step
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i, :, :])  # Adjust indexing based on dimensions of your data
