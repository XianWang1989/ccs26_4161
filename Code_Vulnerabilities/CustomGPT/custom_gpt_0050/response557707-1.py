
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Loop through the time dimension and print precipitation values
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Access the precipitation values for the specific time step
    precip_values = precip[i, :, :]  # Adjust according to dimensions
    precip_values = np.ma.masked_equal(precip_values, 9.969209968386869e+36)  # Mask the erroneous value

    print(precip_values)
