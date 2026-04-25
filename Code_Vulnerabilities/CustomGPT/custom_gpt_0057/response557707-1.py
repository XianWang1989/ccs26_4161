
import numpy as np
import netCDF4

f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

for i in range(len(time)):
    print("Precipitation for year:", time[i])
    year_precip = precip[i, :, :]  # Adjust slicing to access the correct arrays
    print(year_precip)

f.close()
