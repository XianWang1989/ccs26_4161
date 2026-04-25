
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract dimensions and variables from the NetCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjusting dtype

# Loop through the time dimension
for i in range(len(time)):
    print(f"Precipitation for year {time[i]}:")

    # Check for valid precipitation values (e.g., avoiding the fill value)
    valid_precip = np.ma.masked_equal(precip[i, :, :], 9.969209968386869e+36)

    # Print the valid precipitation values
    print(valid_precip)
