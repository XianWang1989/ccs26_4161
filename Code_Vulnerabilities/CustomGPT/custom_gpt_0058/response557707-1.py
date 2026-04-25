
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming 'pre' is a 3D variable: [time, lat, lon]
# Find the fill value for precipitation
fill_value = f.variables['pre']._ FillValue

# Loop over each time index
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Mask the fill value
    valid_precip = np.ma.masked_equal(precip[i], fill_value)

    # Check if there are any valid data points
    if valid_precip.count() > 0:
        print(valid_precip)
    else:
        print("No valid precipitation data for this time index.")
