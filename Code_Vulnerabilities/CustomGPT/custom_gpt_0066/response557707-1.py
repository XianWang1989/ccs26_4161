
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Read the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the valid missing value that might be set in the netCDF attributes
missing_value = f.variables['pre'].missing_value

# Iterate through each time step
for i in range(len(time)):
    precip_data = precip[i]

    # Mask out the missing values
    precip_data = np.ma.masked_equal(precip_data, missing_value)

    print(f"Precipitation for Year {time[i]}:")
    print(precip_data)
