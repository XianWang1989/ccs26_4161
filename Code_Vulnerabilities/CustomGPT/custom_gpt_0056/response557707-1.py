
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Define dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Example of a mask for invalid values
# Here, I assume that '9.969209968386869e+36' is an invalid value for precipitation.
invalid_value = 9.969209968386869e+36
mask = precip != invalid_value

for i in range(len(time)):
    print("Precipitation for year index:", i)
    yearly_precip = precip[i][mask[i]]

    if yearly_precip.size > 0:
        print(yearly_precip)  # Output the valid precipitation values
    else:
        print("No valid precipitation data available for this year.")

# Don't forget to close the dataset
f.close()
