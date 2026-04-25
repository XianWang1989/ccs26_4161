
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='netCDF4')

# Retrieve the variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Load precipitation data

# Define the fill value (this is often the default fill value for netCDF)
fill_value = f.variables['pre']._FillValue

# Loop through each time step and check for the fill value
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Filter out fill values
    valid_precip = np.where(precip[i] != fill_value, precip[i], np.nan)

    # Print only valid precipitation values
    print(valid_precip)
