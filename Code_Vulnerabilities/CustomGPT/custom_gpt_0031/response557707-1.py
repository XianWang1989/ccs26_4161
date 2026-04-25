
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Retrieve dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Read precipitation data

# Define the invalid value (e.g., 9.969209968386869e+36)
invalid_value = 9.969209968386869e+36

# Loop through the time dimension
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Get precipitation data for the current time step
    precip_data = precip[i]

    # Mask out the invalid values
    valid_precip = np.where(precip_data != invalid_value, precip_data, np.nan)

    # Print valid precipitation values, ignoring NaN entries
    print(valid_precip[~np.isnan(valid_precip)])
