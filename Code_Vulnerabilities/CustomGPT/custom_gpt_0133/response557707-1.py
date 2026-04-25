
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Get the dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' is the precipitation variable

# Loop through each time index and print the corresponding precipitation values.
for i in range(len(time)):
    print("Precipitation for year index:", i)
    yearly_precip = precip[i, :, :]  # Access the precipitation for the specific time index

    # Check for invalid values and set them to np.nan or other desired value
    yearly_precip[yearly_precip >= 1e20] = np.nan  # Example threshold for masking

    print(yearly_precip)
