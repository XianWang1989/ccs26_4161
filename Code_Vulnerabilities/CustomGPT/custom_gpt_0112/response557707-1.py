
import netCDF4
import numpy as np

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Iterate over time indices and print precipitation values
for i in range(len(time)):
    print("Precipitation for year index:", i)
    year_precip = precip[i, :, :]  # Adjust dimensions as needed (time, lat, lon)

    # Mask the invalid values (if they are set to the large number you mentioned)
    year_precip = np.where(year_precip == 9.969209968386869e+36, np.nan, year_precip)

    print(year_precip)
