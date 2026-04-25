
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjusted dtype

# Get fill value and mask
fill_value = f.variables['pre'].getncattr('_FillValue')
precip = np.where(precip == fill_value, np.nan, precip)

# Loop through time and print precipitation
for i in range(len(time)):
    print("Precipitation for time index:", i)
    print(precip[i])
