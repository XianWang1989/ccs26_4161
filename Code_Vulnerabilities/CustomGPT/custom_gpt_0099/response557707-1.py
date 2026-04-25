
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Retrieve dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check the fill value for the precipitation data
fill_value = f.variables['pre']._FillValue

# Loop through time and print precipitation values while ignoring the fill value
for i in range(len(time)):
    precip_value = precip[i]

    # Mask out fill values
    if precip_value != fill_value:
        print("Precipitation for year {}: {}".format(time[i], precip_value))
    else:
        print("Precipitation for year {}: No data".format(time[i]))

f.close()
