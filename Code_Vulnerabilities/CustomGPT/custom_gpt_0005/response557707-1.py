
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Read the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define a missing value (common in NetCDF files)
missing_value = f.variables['pre']._FillValue

# Loop through each time step and print precipitation values
for i in range(len(time)):
    precipitation_data = precip[i]

    # Replace missing values with np.nan or remove them
    precipitation_data[precipitation_data == missing_value] = np.nan

    print(f"Precipitation for year {time[i]}:")
    print(precipitation_data)
