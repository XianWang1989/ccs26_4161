
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Load precipitation data

# Replace the large number with np.nan (assuming it's the missing value)
missing_value = 9.969209968386869e+36  # Example of the missing value indicator
precip = np.where(precip == missing_value, np.nan, precip)

# Loop through time indices
for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(precip[i])  # Print the precipitation for the current time index

# Close the dataset
f.close()
