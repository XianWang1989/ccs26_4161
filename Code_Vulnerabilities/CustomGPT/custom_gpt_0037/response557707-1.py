
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Masking the precipitation values to avoid large numbers
masked_precip = np.ma.masked_equal(precip, 9.969209968386869e+36)

# Loop through the time dimension and print precipitation for each year
for i in range(len(time)):
    print("Precipitation for:", time[i])
    print(masked_precip[i])  # Accessing the i-th time slice
