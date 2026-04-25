
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value (you might need to check the specific variable's attributes)
fill_value = f.variables['pre']._FillValue

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for:", time[i])
    valid_precip = np.ma.masked_equal(precip[i], fill_value)  # Mask fill values
    print(valid_precip)
