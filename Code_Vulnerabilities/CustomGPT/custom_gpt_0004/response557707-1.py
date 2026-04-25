
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Replace the large placeholder value with NaN for easier filtering
placeholder_value = 9.969209968386869e+36
precip[precip == placeholder_value] = np.nan

for i in range(len(time)):
    print("Precipitation for:", time[i])
    precip_data = precip[i, :, :]  # Assuming precip has dimensions (time, lat, lon)

    # Masking invalid data
    masked_precip = np.ma.masked_invalid(precip_data)

    print(masked_precip)
