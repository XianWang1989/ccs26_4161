
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming 'time' is one-dimensional and matches 'precip' dimensions
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extract the precipitation for the current time index
    precip_current = precip[i, :, :]  # Adjust indexing as needed based on the shape of 'precip'

    # Replace the large number with NaN for missing values (if applicable)
    precip_current[precip_current == 9.969209968386869e+36] = np.nan

    print(precip_current)

# Close the dataset
f.close()
