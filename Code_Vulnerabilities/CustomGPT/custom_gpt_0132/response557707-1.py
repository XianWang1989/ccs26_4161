
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the missing value (replace this with the actual missing value for your dataset)
missing_value = 9.969209968386869e+36

# Loop through the time variable and print non-missing precipitation values
for i in range(len(time)):
    current_precip = precip[i]
    # Mask the missing values
    valid_precip = np.ma.masked_equal(current_precip, missing_value)

    print(f"Precipitation for time index {i} ({time[i]}):")
    print(valid_precip)
