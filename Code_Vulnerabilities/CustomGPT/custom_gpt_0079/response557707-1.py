
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Get the dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' is the variable for precipitation

# Loop through each time point
for index in range(len(time)):
    # Extract precipitation for the current time index
    precip_values = precip[index, :, :]  # Access the 2D precipitation data for this time index
    # Check if any values are not the fill value
    if np.any(precip_values != 9.969209968386869e+36):
        print("Precipitation for year index", index, ":", precip_values)
    else:
        print("Precipitation for year index", index, "is a fill value.")
