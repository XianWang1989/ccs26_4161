
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get dimensions and variables
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
time = f.variables['time'][:]
precip = f.variables['pre'][:]  # Get the precipitation variable

# Replace fill value (commonly used is 9.969209968386869e+36) with NaN
fill_value = 9.969209968386869e+36
precip = np.where(precip == fill_value, np.nan, precip)

# Loop through the time variable and print precipitation values per year
for i, year in enumerate(time):
    print(f"Precipitation for year {year}: {precip[i]}")  # Adjust this as needed for your data structure
