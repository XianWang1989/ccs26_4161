
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value for the precipitation variable
fill_value = f.variables['pre']._FillValue  # This is often a large number

# Mask fill values in the precipitation data
precip_masked = np.ma.masked_equal(precip, fill_value)

# Loop through time and print the precipitation data
for i in range(len(time)):
    print("Precipitation for year index:", i)
    print(precip_masked[i])  # Access the precipitation for the specific year
