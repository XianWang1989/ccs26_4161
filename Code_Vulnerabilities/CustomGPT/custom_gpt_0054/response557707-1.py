
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Identify the missing value (This might be specific to your data; check the documentation)
missing_value = f.variables['pre']._FillValue  # Check if _FillValue is defined

# Replace missing values with NaN
precip[precip == missing_value] = np.nan

# Loop through the time dimension
for i in range(len(time)):
    print("Precipitation for:", time[i])
    print(precip[i])  # This should output the precipitation values correctly

# Close the dataset when done
f.close()
