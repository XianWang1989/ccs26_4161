
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='netCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjusting dtype just to fetch values without a specific datatype here

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for year index:", i)  # Print the index for clarity
    print(precip[i])  # Extract and print precipitation values for that time index

# Don't forget to close the dataset when done
f.close()
