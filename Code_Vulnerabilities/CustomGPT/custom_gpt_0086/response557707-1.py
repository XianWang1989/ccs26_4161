
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the missing value
missing_value = 9.969209968386869e+36

# Replace missing values with NaN
precip = np.where(precip == missing_value, np.nan, precip)

# Loop through time and print precipitation values, avoiding the NaN values
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    precip_year = precip[i, :, :]  # Assuming time is the first dimension
    if not np.all(np.isnan(precip_year)):
        print(precip_year[~np.isnan(precip_year)])  # Print only valid precipitation values
    else:
        print("No valid precipitation data for this year.")
