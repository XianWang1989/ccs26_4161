
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value (usually stored in the variable)
fill_value = f.variables['pre']._FillValue

# Iterate over each time index and print precipitation data
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Masking the fill values
    prec_data = np.ma.masked_equal(precip[i], fill_value)

    print(prec_data)
