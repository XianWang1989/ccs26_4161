
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the missing value
missing_value = 9.969209968386869e+36

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Create a mask to ignore missing values
    valid_precip = np.ma.masked_equal(precip[i, :, :], missing_value)

    # Print the valid precipitation values
    print(valid_precip)

# Close the dataset
f.close()
