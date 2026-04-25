
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=np.float32)  # Ensure the array type is correct

# Identify the fill value (make sure to check your variable attributes for the correct fill value)
fill_value = netCDF4.default_fillvals['f4']  # Update 'f4' if your data type is different

# Convert fill values to NaN
precip[precip == fill_value] = np.nan

# Iterate over the time dimension to print precipitation data year by year
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i, :, :])
