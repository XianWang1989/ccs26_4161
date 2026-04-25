
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Get dimensions and variables 
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # No need for dtype here; just get the data

# Loop through the time dimension and print precipitation data
for t_index in range(len(time)):  # Iterate over time indices
    print("Precipitation for year:", time[t_index])
    precip_data = precip[t_index, :, :]  # Access precipitation data for that time index
    if np.all(precip_data != 9.969209968386869e+36):  # Check for valid data
        print(precip_data)  # Print only if data is valid
    else:
        print("No valid data for this year.")  # Handle invalid data
