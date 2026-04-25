
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Access the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Obtain the fill value
fill_value = f.variables['pre']._FillValue  # Check for the actual fill value used

# Loop through time and print precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])
    precip_values = precip[i]

    # Mask fill values
    valid_precip = np.ma.masked_equal(precip_values, fill_value)

    # Print only valid precipitation values
    if valid_precip.size > 0:
        print(valid_precip)
    else:
        print("No valid precipitation data available.")
