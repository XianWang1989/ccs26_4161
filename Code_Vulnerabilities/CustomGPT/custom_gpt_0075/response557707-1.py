
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Placeholder value for missing data
missing_value = 9.969209968386869e+36

# Iterate over the time dimension and print valid precipitation values
for i in range(len(time)):
    # Check the corresponding precipitation value
    annual_precip = precip[i]

    # If the data is valid, print it
    if annual_precip != missing_value:
        print(f"Precipitation for year {i}: {annual_precip}")
    else:
        print(f"Precipitation data for year {i} is missing.")
