
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get the dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Correctly store precipitation values

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Assuming you want to print all grid points; otherwise, adjust indexing
    precipitation_value = precip[i, :, :]  # Access the precip for the current time index
    print(precipitation_value)

# Close the dataset
f.close()
