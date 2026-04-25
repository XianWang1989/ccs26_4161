
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check for the fill value typically used in netCDF files
fill_value = f.variables['pre']._FillValue if '_FillValue' in f.variables['pre'].ncattrs() else None

# Iterate over time and extract precipitation values
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Get precipitation values for the current time index
    current_precip = precip[i]

    # Replace the fill values with NaN or any desired value
    if fill_value is not None:
        current_precip[current_precip == fill_value] = np.nan

    print(current_precip)

# Close the dataset
f.close()
