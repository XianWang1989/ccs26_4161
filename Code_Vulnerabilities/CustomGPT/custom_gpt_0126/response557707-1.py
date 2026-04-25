
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value (check the actual fill value if needed)
fill_value = 9.969209968386869e+36  # Example fill value, replace if necessary

# Iterate through the time dimension
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Mask the fill values
    precip_masked = np.ma.masked_equal(precip[i], fill_value)

    # Output the precipitation data, ignoring masked values
    print(precip_masked)
