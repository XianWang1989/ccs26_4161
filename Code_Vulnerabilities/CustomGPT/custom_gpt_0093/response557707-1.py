
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value (adjust if different in your dataset)
fill_value = f.variables['pre']._FillValue

# Iterate through time and extract valid precipitation data
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Mask the fill values
    valid_precip = np.ma.masked_equal(precip[i], fill_value)

    # Print the valid values
    print(valid_precip.compressed())  # Use compressed to omit masked values

f.close()
