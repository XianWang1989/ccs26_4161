
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='netCDF4')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Iterate over time indices
for i in range(len(time)):
    print("Precipitation for year index:", i)
    yearly_precip = precip[i, :, :]  # Get the precipitation data for the specific time index
    print(yearly_precip)

# Close the dataset
f.close()
