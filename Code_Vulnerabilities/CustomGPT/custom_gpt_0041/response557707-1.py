
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Dimensions and variables of the netCDF file
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
time = f.variables['time'][:]
precip = f.variables['pre'][:]

# Define the fill value (adjust based on your netCDF metadata)
fill_value = 9.969209968386869e+36

# Loop through each time step and print precipitation data
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    precip_data = precip[i]  # Get the precipitation for the ith time step

    # Mask the fill values
    precip_data = np.where(precip_data == fill_value, np.nan, precip_data)

    # Print only valid precipitation data (not NaN)
    valid_precip = precip_data[~np.isnan(precip_data)]
    print(valid_precip)
