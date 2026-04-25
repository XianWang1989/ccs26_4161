
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define fill value and mask it
fill_value = f.variables['pre']._FillValue  # Get the fill value for the precipitation variable
masked_precip = np.ma.masked_equal(precip, fill_value)  # Mask the fill value

# Loop through time indices
for t_idx in range(len(time)):
    print("Precipitation for year:", time[t_idx])
    # Extract precipitation for the specific time index
    precip_data = masked_precip[t_idx, :, :]  # Adjust dimensions as necessary
    print(precip_data)

# Close the dataset
f.close()
