
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming time is indexed in a specific way
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Accessing the precipitation data for the current time index
    year_precip = precip[i, :, :]  # Adjust based on your data shape
    print(year_precip)

# Close the dataset
f.close()
