
import numpy as np
import netCDF4

# Open the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Loop through time indices and print precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])
    print(precip[i])  # Assuming precip is indexed by time directly

# Close the dataset
f.close()
