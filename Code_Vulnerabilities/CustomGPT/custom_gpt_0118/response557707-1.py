
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=float)  # Ensure the data type is float

# Define the missing value (adjust if necessary)
missing_value = 9.969209968386869e+36

# Loop through the time variable
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    # Mask the missing values
    precip_masked = np.where(precip[i] == missing_value, np.nan, precip[i])
    print(precip_masked)
