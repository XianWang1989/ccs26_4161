
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  

# Get the fill value (if defined)
fill_value = f.variables['pre'].missing_value  # Check for the actual fill value

# Loop through the time dimension
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Extract precipitation for the current time index
    precip_data = precip[i, :, :]  # Adjust the indexing based on dimensions

    # Filter out the fill value
    if fill_value in precip_data:
        precip_data = np.where(precip_data == fill_value, np.nan, precip_data)

    print(precip_data)
