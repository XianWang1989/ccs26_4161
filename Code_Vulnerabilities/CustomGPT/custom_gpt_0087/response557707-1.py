
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)

# Define a mask for valid data (ignoring the placeholder value)
mask_value = 9.969209968386869e+36
mask = np.ma.masked_equal(precip, mask_value)

# Loop through time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(mask[i])
