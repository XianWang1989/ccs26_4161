
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming the time variable is a 1D index for the precipitation data
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Extract the precipitation data for the given time index
    precip_for_year = precip[i]

    # Use a mask to filter out the invalid value
    valid_precip = np.ma.masked_equal(precip_for_year, 9.969209968386869e+36)

    print(valid_precip)
