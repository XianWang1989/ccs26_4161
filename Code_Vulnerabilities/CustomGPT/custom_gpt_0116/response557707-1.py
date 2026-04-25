
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)

# Identify and handle the missing value
missing_value = f.variables['pre'].missing_value

# Loop through time to get precipitation data
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Mask the missing values
    precip_masked = np.ma.masked_equal(precip[i], missing_value)

    print(precip_masked)
