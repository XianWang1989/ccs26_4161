
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define a valid precipitation value (replace with your known valid value if different)
valid_precip_value = 9.969209968386869e+36  # Example, replace with the actual invalid value

# Loop through time
for i in range(len(time)):
    print("Precipitation for:", time[i])
    valid_precip = precip[i][precip[i] != valid_precip_value]
    print(valid_precip)
