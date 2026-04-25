
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the missing value (based on your output)
missing_value = 9.969209968386869e+36

# Iterate through time and print precipitation
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Get the corresponding precipitation data
    precip_data = precip[i, :, :]  # Adjust indexing based on your dimensions

    # Mask out the missing values
    precip_data = np.where(precip_data == missing_value, np.nan, precip_data)

    # Print the precipitation values, excluding any NaN (previously missing values)
    print(precip_data)

# Close the dataset
f.close()
