
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' stores precipitation values

# Iterate over time indices
for i in range(len(time)):
    print("Precipitation for:", time[i])
    # Access precipitation data for the current time index
    precip_values = precip[i, :, :]  # Adjust indexing based on data shape
    # Use numpy to mask the placeholder value
    precip_values[precip_values == 9.969209968386869e+36] = np.nan  # Replace with NaN for clarity
    print(precip_values)

# Close the netCDF file
f.close()
