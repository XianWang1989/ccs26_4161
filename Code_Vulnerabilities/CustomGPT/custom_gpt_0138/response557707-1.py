
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming -9999 is the fill value, change it based on your netCDF file specifications
fill_value = -9999

# Loop through time dimension and print precipitation
for i in range(len(time)):
    precip_data = precip[i]
    # Mask the fill values
    masked_precip = np.ma.masked_equal(precip_data, fill_value)

    print("Precipitation for year:", time[i])
    print(masked_precip)
