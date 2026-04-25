
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)

# Define the fill value
fill_value = 9.969209968386869e+36

# Iterate over time and print the valid precipitation data
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Using a mask to filter out the fill value
    valid_precip = np.ma.masked_equal(precip[i], fill_value)

    print(valid_precip.compressed())  # Display only valid precipitation values
