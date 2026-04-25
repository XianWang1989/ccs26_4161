
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get the dimensions and variables of the NetCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjust the datatype if necessary

# Loop through the time indices
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i])  # Access data for the specific time index directly

# Close the dataset
f.close()
