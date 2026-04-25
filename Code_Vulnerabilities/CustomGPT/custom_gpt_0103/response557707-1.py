
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value
fill_value = f.variables['pre']._FillValue

# Iterate through time and print precipitation values
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    # Filter out the fill values
    valid_precip = np.where(precip[i] != fill_value, precip[i], np.nan)
    print(valid_precip)  # Output the valid values
