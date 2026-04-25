
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)  # Use float for better handling

# Example of a fill value, adjust based on your netCDF's fill value
fill_value = f.variables['pre']._FillValue

for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Get the precipitation for the current time index
    current_precip = precip[i]

    # Mask out the fill values
    valid_precip = np.where(current_precip == fill_value, np.nan, current_precip)

    # Print the valid precipitation values
    print(valid_precip)
