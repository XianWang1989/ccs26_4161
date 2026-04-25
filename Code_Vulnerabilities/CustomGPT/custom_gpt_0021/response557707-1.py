
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Access dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the missing value (adjust if different in your dataset)
missing_value = 9.969209968386869e+36

# Iterate over each time index
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Mask out the missing values
    valid_precip = np.ma.masked_equal(precip[i], missing_value)

    print(valid_precip)

# Close the dataset
f.close()
