
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)  # Ensure correct data type

# Define the fill value
fill_value = 9.969209968386869e+36

# Create a masked array that ignores fill values
masked_precip = np.ma.masked_where(precip == fill_value, precip)

for i, year in enumerate(time):
    print("Precipitation for year:", year)

    # Print the precipitation values for the current year
    print(masked_precip[i])  # This will only show valid precipitation values
