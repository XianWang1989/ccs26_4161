
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Determine the fill value (commonly used in netCDF files)
fill_value = f.variables['pre']._FillValue

# Iterate over each time index and print precipitation values
for t_index in range(len(time)):
    print("Precipitation for time index:", t_index)

    # Extract the precipitation data for that specific time
    precip_values = precip[t_index, :, :]  # Assuming [time, lat, lon] dimensions
    # Masking fill values
    precip_values = np.ma.masked_equal(precip_values, fill_value)

    print(precip_values)
