
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Access the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming that time is a 1D array of indices for precipitation
for t in range(len(time)):
    print("Precipitation for year:", time[t])

    # Extracting precipitation values for the specific time index
    precip_values = precip[t, :, :]  # Adjust as needed depending on data dimensions

    # Check for valid values (not the missing value indicator)
    if np.all(precip_values == 9.969209968386869e+36):
        print("No valid precipitation data for this time")
    else:
        # Mask the invalid data
        precip_values_masked = np.ma.masked_equal(precip_values, 9.969209968386869e+36)
        print(precip_values_masked)
