
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Load precipitation data

# Define the fill value (check your netCDF to confirm this value)
fill_value = 9.969209968386869e+36

# Iterate through each time index
for i in range(len(time)):
    yearly_precip = precip[i]  # Select the relevant slice for this year

    # Mask the fill values
    if np.any(yearly_precip == fill_value):
        yearly_precip = np.ma.masked_equal(yearly_precip, fill_value)

    print("Precipitation for year {}: {}".format(time[i], yearly_precip))
