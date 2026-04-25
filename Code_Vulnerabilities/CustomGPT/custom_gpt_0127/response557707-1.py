
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Getting the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:]) 

# Define a fill value if it's defined in the dataset
fill_value = f.variables['pre']._FillValue if hasattr(f.variables['pre'], '_FillValue') else None

# Iterate through each time index
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Mask the fill values in precip
    masked_precip = np.ma.masked_equal(precip[i, :, :], fill_value)
    print(masked_precip)
