
import numpy as np
import netCDF4

# Load the netCDF file
file_path = 'Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc'
dataset = netCDF4.Dataset(file_path, 'r')

# Get the variables
lon = np.array(dataset.variables['lon'][:])
lat = np.array(dataset.variables['lat'][:])
time = np.array(dataset.variables['time'][:])
precip = dataset.variables['pre']

# Iterate over each time step
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extracting precipitation for the current time step
    precip_data = precip[i, :, :]  # Adjust the indexing as necessary for your data structure
    print(precip_data)

# Close the dataset
dataset.close()
