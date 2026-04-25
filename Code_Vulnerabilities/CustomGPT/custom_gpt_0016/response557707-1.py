
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='netCDF4')

# Read in the variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Determine the fill value
fill_value = f.variables['pre']._FillValue if '_FillValue' in f.variables['pre'].ncattrs() else None

# Loop through each time step
for i in range(len(time)):
    print(f"Precipitation for year {time[i]}:")

    # Get the precipitation for the current time step
    precip_data = precip[i, :, :]

    # Use numpy to create a masked array to ignore fill values
    precip_masked = np.ma.masked_equal(precip_data, fill_value)

    # Print the precipitation values, excluding fill values
    if precip_masked.count() > 0:
        print(precip_masked)
    else:
        print("No valid precipitation data available for this time step.")

# Close the dataset
f.close()
