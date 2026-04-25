
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Define the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming that your fill value is 9.969209968386869e+36
fill_value = 9.969209968386869e+36

# Replace fill value with NaN
precip = np.where(precip == fill_value, np.nan, precip)

for i in range(len(time)):
    print("Precipitation for year:", time[i])
    # Print the precipitation data for the specific year, removing NaN values
    year_precip = precip[i, :, :]

    # Mask NaN values to prevent them from printing
    valid_precip = year_precip[~np.isnan(year_precip)]

    print(valid_precip)
