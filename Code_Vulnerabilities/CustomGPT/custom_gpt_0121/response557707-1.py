
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check the NetCDF variable's fill_value (if defined)
fill_value = f.variables['pre']._FillValue  # Retrieve the fill value

# Extract precipitation data for each time step
for i in range(len(time)):
    precip_value = precip[i]  # Get precipitation for the current time step
    if precip_value != fill_value:  # Check if it’s not the fill value
        print("Precipitation for:", time[i])
        print(precip_value)
    else:
        print("No valid precipitation data for:", time[i])

# Close the dataset
f.close()
