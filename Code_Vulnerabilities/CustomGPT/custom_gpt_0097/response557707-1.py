
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Access dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value (usually should be checked in the netCDF file attributes)
fill_value = f.variables['pre']._FillValue

# Loop through each timestep and print non-fill precipitation data
for i in range(len(time)):
    print("Precipitation for year index:", i)
    # Mask fill values
    valid_precip = np.ma.masked_equal(precip[i], fill_value)
    print(valid_precip)
