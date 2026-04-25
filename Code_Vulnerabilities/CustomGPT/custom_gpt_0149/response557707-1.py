
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value (check your netCDF file for the actual fill value)
fill_value = 9.969209968386869e+36 

# Iterate through time and print precipitation
for i in range(len(time)):
    precip_data = precip[i]  # Extract data for the specific time index
    # Mask the fill values
    precip_data = np.ma.masked_equal(precip_data, fill_value)

    print("Precipitation for year", time[i])
    print(precip_data)

# Close the dataset
f.close()
