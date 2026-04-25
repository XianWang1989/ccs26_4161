
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Use appropriate dtype if needed

# Define the fill value (this should match the fill value in your dataset)
fill_value = 9.969209968386869e+36

for i in range(len(time)):
    # Extract precipitation data for the current time index
    current_precip = precip[i, :, :]  # Assuming 3D data: time, lat, lon

    # Mask the fill values
    current_precip_masked = np.ma.masked_equal(current_precip, fill_value)

    print(f"Precipitation for: {time[i]}")
    # Print only the non-fill values
    print(current_precip_masked)
