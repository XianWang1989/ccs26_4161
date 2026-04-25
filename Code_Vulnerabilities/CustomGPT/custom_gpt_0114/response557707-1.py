
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the missing value as per your dataset's documentation
missing_value = 9.969209968386869e+36  # Example missing value

# Iterate over time
for i in range(len(time)):
    precip_values = precip[i, :, :]  # Get the precipitation for the current time step
    # Mask the missing values
    precip_values = np.ma.masked_where(precip_values == missing_value, precip_values)

    # Print the precipitation only if it's not masked
    print("Precipitation for:", time[i])
    if precip_values.size > 0:
        print(precip_values)
