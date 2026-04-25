
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the invalid value
invalid_value = 9.969209968386869e+36

# Iterate through time and print precipitation, masking the invalid values
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Mask invalid values in the precipitation data
    valid_precip = np.where(precip[i] == invalid_value, np.nan, precip[i])  # Replace invalid values with NaN
    print(valid_precip[~np.isnan(valid_precip)])  # Print only valid values
