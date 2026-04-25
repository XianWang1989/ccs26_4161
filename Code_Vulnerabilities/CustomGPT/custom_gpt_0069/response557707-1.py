
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming the fill value is a common large number; adjust as needed.
fill_value = 9.969209968386869e+36  # Example fill value, replace if different

# Loop through the time variable and print precipitation values, handling missing data
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Extract precipitation for the current time index
    precip_data = precip[i]

    # Mask out the fill values
    precip_data = np.where(precip_data == fill_value, np.nan, precip_data)
    valid_precip = precip_data[~np.isnan(precip_data)]  # Remove NaN values

    print(valid_precip)
