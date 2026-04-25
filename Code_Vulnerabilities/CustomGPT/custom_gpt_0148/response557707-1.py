
import numpy as np
import netCDF4 as nc

# Load the netCDF file
f = nc.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Define variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Read the entire 'pre' variable

# Get the fill value, if defined
fill_value = f.variables['pre']._FillValue if '_FillValue' in f.variables['pre'].ncattrs() else None

for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Avoid fill values
    year_precip = np.where(precip[i] == fill_value, np.nan, precip[i])  # Replace fill values with NaN
    print(year_precip)
