
import numpy as np
import netCDF4

# Load the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get variables
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
time = f.variables['time'][:]
precip = f.variables['pre'][:]

# Assuming precip is a 3D array (time, lat, lon)
# Define a missing value placeholder (check the attributes in your file)
missing_value = f.variables['pre']._fillvalue  # or set it explicitly if known

# Loop through the time dimension
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Get the precipitation data for this specific time step
    precip_data = precip[i, :, :]

    # Mask the missing values
    precip_data = np.ma.masked_equal(precip_data, missing_value)

    # Print the masked precipitation data
    print(precip_data)

# Close the dataset
f.close()
