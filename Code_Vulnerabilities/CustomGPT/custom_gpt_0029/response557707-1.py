
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  

# Check for fill value and mask it
fill_value = f.variables['pre']._FillValue  # Get the fill value from the variable
precip = np.ma.masked_equal(precip, fill_value)

# Loop through the time variable
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i])  # Print precipitation data for the year
