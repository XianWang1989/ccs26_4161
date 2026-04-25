
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Make sure to read correctly here

# Iterate through time and extract precipitation
for i in range(len(time)):
    print("Precipitation for:", time[i])
    # Replace with an appropriate time index if necessary
    precip_values = precip[i, :, :]  # Assuming 'pre' is 3D (time, lat, lon)

    # Optionally handle the large number issue
    precip_values[precip_values >= 1e20] = np.nan  # Set unrealistic values to NaN or an appropriate mask

    print(precip_values)
