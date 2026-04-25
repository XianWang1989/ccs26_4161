
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the placeholder value (usually, netCDF stores missing data as a specific value)
missing_value = f.variables['pre'].missing_value  # or you can define it manually, e.g., 9.969209968386869e+36

# Iterate through each time step
for i in range(len(time)):
    # Mask the precip array to only show valid values
    precip_masked = np.ma.masked_where(precip[i] == missing_value, precip[i])

    print("Precipitation for year:", time[i])
    print(precip_masked)
