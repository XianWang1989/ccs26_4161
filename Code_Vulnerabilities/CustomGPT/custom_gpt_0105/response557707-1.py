
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Get the variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' holds precipitation data

# Iterate over each time index
for i in range(len(time)):
    print("Precipitation for time index:", i)

    # Access the precipitation data for the current time index
    precip_data = precip[i, :, :]  # Adjust if dimensions require it
    precip_data_masked = np.ma.masked_equal(precip_data, 9.969209968386869e+36)  # Mask the large value

    print(precip_data_masked)
