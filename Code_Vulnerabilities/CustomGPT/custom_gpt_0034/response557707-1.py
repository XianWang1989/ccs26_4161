
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Load dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # No need to specify dtype here

# Get the fill value (you might need to check your dataset for this)
fill_value = f.variables['pre']._FillValue

# Replace fill value with NaN
precip[precip == fill_value] = np.nan

# Iterate over time and print precipitation for each year
for t in range(len(time)):
    print("Precipitation for time index:", t)
    valid_precip = precip[t, :, :]  # Accessing the precipitation for the specific time index
    print(valid_precip[~np.isnan(valid_precip)])  # Print only valid precipitation values
