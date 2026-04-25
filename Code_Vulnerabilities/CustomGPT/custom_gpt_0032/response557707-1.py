
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Access dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Remove dtype specification

# Define a fill value (this may vary depending on your dataset)
fill_value = f.variables['pre']._FillValue  # Get the fill value from the dataset

# Loop through each time step
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Retrieve the precipitation values for the current time step
    precip_values = precip[i, :, :]

    # Mask out the fill values
    precip_values = np.ma.masked_equal(precip_values, fill_value)

    print(precip_values)
