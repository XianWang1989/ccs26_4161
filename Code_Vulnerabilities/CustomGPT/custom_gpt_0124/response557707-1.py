
import numpy as np
import netCDF4 as nc

# Load the NetCDF file
f = nc.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the NetCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Fill value (check your NetCDF file for the actual fill value)
fill_value = f.variables['pre']._fill_value

# Loop through each time index
for i in range(len(time)):
    # Mask the precipitation data to remove fill values
    masked_precip = np.ma.masked_equal(precip[i], fill_value)

    print(f"Precipitation for time index {i}:")
    print(masked_precip)
