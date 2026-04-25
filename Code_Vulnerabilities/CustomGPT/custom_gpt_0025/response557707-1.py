
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Correctly extract the precipitation data

# Iterate over time indices and print precipitation
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i])  # Access the precipitation data for the specific time index
