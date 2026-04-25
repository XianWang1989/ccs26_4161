
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Retrieve dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value according to your dataset
fill_value = 9.969209968386869e+36

# Loop through each time index
for i in range(len(time)):
    # Fetch the precipitation data for the current time index
    precip_data = precip[i, :, :]

    # Replace the fill value with NaN or omit it from the output
    precip_data[precip_data == fill_value] = np.nan  # or use np.ma.masked_where to mask it

    print(f"Precipitation for year {time[i]}:")
    print(precip_data)
