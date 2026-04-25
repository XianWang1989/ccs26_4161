
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjusted this line to correctly fetch the precip variable

# Assuming the missing value is 9.969209968386869e+36
missing_value = 9.969209968386869e+36

# Loop through time and print precipitation
for i in range(len(time)):
    print("Precipitation for:", time[i])
    precip_data = precip[i, :, :]  # Adjust indexing as needed

    # Replace missing values with np.nan
    precip_data[precip_data == missing_value] = np.nan

    # Print the filtered precipitation data
    print(precip_data)
