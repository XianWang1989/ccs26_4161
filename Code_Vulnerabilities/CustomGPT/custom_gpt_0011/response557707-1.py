
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Make sure to correctly extract the 'pre' variable

# Define the no-data value to filter out
no_data_value = 9.969209968386869e+36  # This is the value you wish to avoid

# Loop through each time index and print precipitation data
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Get precipitation data for the specific time index
    precip_data = precip[i]

    # Use numpy to mask out the no-data values from the output
    if isinstance(precip_data, np.ndarray):
        precip_data = np.where(precip_data == no_data_value, np.nan, precip_data)  # Replace with NaN
    else:
        precip_data = np.nan if precip_data == no_data_value else precip_data

    print(precip_data)
