
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Removed dtype to ensure we get the right data

# Assuming the first dimension is time, and replacing invalid values
for i in range(len(time)):
    yearly_precip = precip[i, :, :]  # Accessing the precipitation for the current time index
    if np.any(yearly_precip == 9.969209968386869e+36):  # Check against the invalid value
        yearly_precip[yearly_precip == 9.969209968386869e+36] = np.nan  # Replace it with NaN
    print("Precipitation for year index:", i)
    print(yearly_precip)
