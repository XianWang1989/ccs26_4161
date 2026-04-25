
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming that the fill value for precipitation is what you're encountering
# You may need to check the specific fill value in your dataset
fill_value = 9.969209968386869e+36

# Create a masked array to ignore the fill values
masked_precip = np.ma.masked_equal(precip, fill_value)

# Loop through each time step and print the precipitation
for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(masked_precip[i])  # Only prints non-masked, valid precipitation values
