
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Read the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Ensure this correctly captures the precipitation data

# Iterate through the time dimension and print precipitation data
for i in range(len(time)):
    print("Precipitation for:", time[i])
    # Access the precipitation data using the time index
    precip_value = precip[i, :, :]  # Assuming precip is 3D (time, lat, lon)
    print(precip_value)

# Close the dataset
f.close()
