
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define a mask for valid values (assuming 9.969209968386869e+36 is invalid)
valid_precip_mask = (precip != 9.969209968386869e+36)

# Loop through each time step and print precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Use the mask to filter valid precipitation values
    filtered_precip = precip[i][valid_precip_mask[i]]
    if filtered_precip.size > 0:
        print(filtered_precip)
    else:
        print("No valid precipitation data available.")

# Close the dataset
f.close()
