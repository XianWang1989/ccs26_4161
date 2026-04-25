
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Retrieve dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming 'time' is correctly defined, and we're interested in the index for each year
# Adjust indexing based on how 'time' relates to 'precip', for example if time is an index or a specific time step

for i in range(len(time)):
    print("Precipitation for time index:", i)
    # Check for valid index before accessing precip data
    if i < precip.shape[0]:  # Ensure we don't go out of bounds
        print(precip[i])
    else:
        print("Index out of range for precipitation data.")

# Close the dataset
f.close()
