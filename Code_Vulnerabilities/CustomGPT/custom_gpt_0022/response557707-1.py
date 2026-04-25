
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define a mask for missing values
missing_value = 9.969209968386869e+36
precip[precip == missing_value] = np.nan  # Replace placeholder with NaN

# Iterate through time and output precipitation
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    valid_precip = precip[i, :, :]  # Select data for the current year
    if np.any(~np.isnan(valid_precip)):  # Check for valid data
        print(valid_precip)
    else:
        print("No valid precipitation data for this year.")
