
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value, if it exists
fill_value = f.variables['pre']._FillValue

# Loop through each time step and print precipitation
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Mask fill values
    precip_data = precip[i]
    precip_data[precip_data == fill_value] = np.nan  # Replace fill values with NaN

    print(precip_data)
