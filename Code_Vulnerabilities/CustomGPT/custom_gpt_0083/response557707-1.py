
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Identify and replace fill value (assuming 9.969209968386869e+36 is the fill value)
fill_value = 9.969209968386869e+36
precip[precip == fill_value] = np.nan  # Set fill values to NaN for easier handling

# Loop through each time index and print precipitation
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i, :, :])  # Use the i-index to access specific time slices
