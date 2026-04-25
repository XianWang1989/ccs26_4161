
import numpy as np
import netCDF4 as nc

# Load the netCDF file
f = nc.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the fill value (assuming it's defined in the attributes)
fill_value = f.variables['pre']._FillValue

# Loop through each time step and print valid precipitation data
for t in range(len(time)):
    print("Precipitation for:", time[t])

    # Get the precipitation for that time step
    precip_data = precip[t]

    # Mask out the fill values
    precip_data_masked = np.ma.masked_equal(precip_data, fill_value)

    # Print only valid data
    if precip_data_masked.count() > 0:
        print(precip_data_masked)
    else:
        print("No valid precipitation data for this time step.")
