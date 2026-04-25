
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjust to get the whole precipitation array

# Check for missing values. Adjust this threshold based on your dataset specifics
missing_value = -9999  # Modify this to your specific dataset's missing value

# Iterate through time and print valid precipitation data
for i in range(len(time)):
    print(f"Precipitation for index {i} ({time[i]}):")

    # Extract precipitation for the specific time frame
    yearly_precip = precip[i]

    # Check for missing values
    if np.all(yearly_precip == missing_value):
        print("No valid data available for this time.")
    else:
        # Filter out the missing values
        valid_precip = np.ma.masked_equal(yearly_precip, missing_value)
        print(valid_precip)
