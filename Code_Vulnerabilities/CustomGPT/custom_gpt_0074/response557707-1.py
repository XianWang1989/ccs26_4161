
import arcpy
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value from the data variable's attributes
fill_value = f.variables['pre'].missing_value  # or you may need to check for _FillValue attribute

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for:", i)

    # Check for missing values and handle accordingly
    precip_data = precip[i]
    precip_data[precip_data == fill_value] = np.nan  # Replace fill values with NaN

    print(precip_data)
