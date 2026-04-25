
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check for fill values
fill_value = f.variables['pre']._FillValue  # Get the fill value

# Loop through each time step
for i in range(len(time)):
    current_precip = precip[i]

    # Mask the fill value
    current_precip[current_precip == fill_value] = np.nan  # Replace fill value with NaN

    print("Precipitation for year {}: {}".format(time[i], current_precip))
