
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Retrieve dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Load precipitation data

# Define a valid value (not equal to the missing value indicator)
valid_precip_value = -9999  # Adjust this based on your dataset's missing value

for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Extract precipitation for the current time index
    current_precip = precip[i]

    # Mask invalid values
    current_precip = np.where(current_precip == valid_precip_value, np.nan, current_precip)

    # Print the valid precipitation values
    print(current_precip[~np.isnan(current_precip)])  # Exclude NaN values
