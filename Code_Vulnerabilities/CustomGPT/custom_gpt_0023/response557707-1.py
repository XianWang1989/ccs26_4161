
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  

# Define the missing value
missing_value = 9.969209968386869e+36

# Loop through time to print precipitation for each year
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extracted precipitation for the current index
    current_precip = precip[i]

    # Mask the missing values
    masked_precip = np.ma.masked_where(current_precip == missing_value, current_precip)

    # Print the resulting precipitation values
    print(masked_precip)

# Close the dataset
f.close()
