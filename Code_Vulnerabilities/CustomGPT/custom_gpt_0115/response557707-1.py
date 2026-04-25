
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define fill value (adjust if necessary based on your dataset)
fill_value = 9.969209968386869e+36

# Loop through each time step
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Mask fill values
    masked_precip = np.ma.masked_equal(precip[i, :, :], fill_value)

    # Print masked precipitation
    print(masked_precip)
