
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

# Identify the fill value (usually a large number like 9.969209968386869e+36)
fill_value = 9.969209968386869e+36

# Replace the fill value with NaN
precip = np.where(precip == fill_value, np.nan, precip)

# Loop through each time step to print precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])
    print(precip[i, :, :])  # Assuming precip is 3D (time, lat, lon)

# Close the dataset
f.close()
