
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Mask the precipitation data for the missing value
missing_value = -9999  # Replace this with the actual missing value if known
precip[precip == missing_value] = np.nan  # Replace with NaN

# Print precipitation for each time step, ensuring values do not repeat
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i, :, :])  # Assuming precip is 3D (time, lat, lon)
