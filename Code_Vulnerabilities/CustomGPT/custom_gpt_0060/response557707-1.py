
import arcpy
import numpy as np
import netCDF4

# Open the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check for the fill value
fill_value = f.variables['pre']._FillValue

# Loop over time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Creating a masked array to ignore fill values
    masked_precip = np.ma.masked_equal(precip[i], fill_value)

    # Print valid precipitation values
    print(masked_precip)
