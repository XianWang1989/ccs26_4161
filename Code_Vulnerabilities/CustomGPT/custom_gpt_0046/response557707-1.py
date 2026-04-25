
import numpy as np
import netCDF4

# Open netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Get the precipitation variable

# Get the fill value for 'pre'
fill_value = f.variables['pre'].getncattr('missing_value')  # or check for '_FillValue'
# Convert to a numpy float for comparison
fill_value = np.float64(fill_value)

# Iterate through time and print valid precipitation values
for i in range(len(time)):
    valid_precip = np.ma.masked_equal(precip[i, :, :], fill_value)  # Mask the fill values
    print("Precipitation for year {}:".format(i))
    print(valid_precip)
