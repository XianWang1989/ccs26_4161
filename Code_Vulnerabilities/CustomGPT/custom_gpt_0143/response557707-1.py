
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Load the variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)  # Ensure it is float

# Define a mask for valid precipitation values
valid_precip_mask = precip != 9.969209968386869e+36  # Define your invalid value

# Loop through time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    valid_precip = precip[i][valid_precip_mask[i]]  # Filter using the mask
    if valid_precip.size > 0:
        print(valid_precip)
    else:
        print("No valid precipitation data for this year.")
