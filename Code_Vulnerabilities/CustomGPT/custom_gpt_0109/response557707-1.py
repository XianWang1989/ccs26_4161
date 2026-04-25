
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjust this line based on your variable

# Iterate over time indices
for i in range(len(time)):
    precipitation_data = precip[i, :, :]  # Access the 2D slice for the specific time index
    # Check for valid data (replace with np.nan where the value is missing)
    precipitation_data[precipitation_data > 1e30] = np.nan  # or appropriate threshold for your data

    print("Precipitation for year index:", i)
    print(precipitation_data)

# Close the dataset
f.close()
