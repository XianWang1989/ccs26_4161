
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Retrieve dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check for missing value attribute if available
missing_value = f.variables['pre'].missing_value if 'missing_value' in f.variables['pre'].ncattrs() else np.nan

# Loop through the time dimension
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    # Filter out the missing values
    valid_precip = np.ma.masked_equal(precip[i], missing_value)

    # Print valid precipitation values
    print(valid_precip.compressed())
