
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Retrieve dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)  # Ensure precip is float

# Define the placeholder value for missing data
missing_value = 9.969209968386869e+36

# Iterate through each time step
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Mask the precipitation data to hide the missing values
    masked_precip = np.ma.masked_equal(precip[i, :, :], missing_value)

    # Print the masked precipitation data
    print(masked_precip)
