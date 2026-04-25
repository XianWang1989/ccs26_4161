
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value (known from netCDF specification)
fill_value = 9.969209968386869e+36  # Example fill value, verify in your netCDF metadata

# Iterate over time to extract precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extract precipitation for the current time index and mask the fill values
    precip_values = precip[i, :, :]  # Assuming precip is 3D: (time, lat, lon)
    precip_values_masked = np.where(precip_values == fill_value, np.nan, precip_values) 

    # Print only the values that are not NaN
    print(precip_values_masked[~np.isnan(precip_values_masked)])
