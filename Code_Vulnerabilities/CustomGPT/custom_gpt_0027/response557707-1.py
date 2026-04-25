
import arcpy
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Get the entire precipitation data array

# Get the fill value (often it's a high number like 9.969209968386869e+36)
fill_value = f.variables['pre'].getncattr('_FillValue')

# Loop through each time step
for i in range(len(time)):
    # Extract precipitation for the given time index
    current_precip = precip[i, :, :]

    # Remove the fill value
    current_precip[current_precip == fill_value] = np.nan  # or use numpy masked arrays

    print("Precipitation for:", time[i])
    print(current_precip)
