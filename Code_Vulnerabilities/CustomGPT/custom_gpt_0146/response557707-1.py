
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Access the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' is the variable for precipitation

# Loop through the time indices, not the time values
for i in range(len(time)):
    # Print the time value (assuming it's datetime-like)
    print("Precipitation for year index:", i)

    # Print the corresponding precipitation data by indexing into precip
    print(precip[i])  # Adjust depending on how precip is structured

# Close the netCDF file
f.close()
