
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Load the dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Ensure correct data type

# Loop through time index and extract precipitation values
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Access the precipitation data for the current time index
    precip_values = precip[i, :, :]  # Assuming precip is 3D (time, lat, lon)

    # Check if the values are valid (excluding the repeating number)
    if np.any(precip_values != 9.969209968386869e+36):  # Replace with NaN or your specific filter
        print(precip_values[precip_values != 9.969209968386869e+36])
    else:
        print("No valid precipitation data for this year.")
