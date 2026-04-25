
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:]) # Adjust the dtype if necessary

# Assuming that `9.969209968386869e+36` is the fill value
fill_value = 9.969209968386869e+36

# Loop through the time array
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Get the precipitation for the current time index
    precip_data = precip[i]

    # Mask the fill values
    masked_precip = np.ma.masked_where(precip_data == fill_value, precip_data)

    # If you want to exclude the fill values and print valid data only
    if np.any(~masked_precip.mask):
        print(masked_precip.compressed())  # Print only values that are not masked
    else:
        print("No valid precipitation data for this year.")
