
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Identify the fill value (e.g., 9.969209968386869e+36)
fill_value = 9.969209968386869e+36

# Loop through the time variable
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Mask the fill value
    precip_masked = np.ma.masked_equal(precip[i], fill_value)

    # Print the masked precipitation values
    print(precip_masked)
