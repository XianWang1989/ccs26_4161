
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Load precipitation data directly

# Ensure that your time variable is indexed correctly
for t_index in range(len(time)):
    print("Precipitation for year index:", t_index)
    current_precip = precip[t_index, :, :]  # Access the precipitation data for the current time index
    print(current_precip)

# Close the netCDF dataset
f.close()
