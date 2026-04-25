
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjusted dtype

# Iterate over the time dimension
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extract precipitation data for the current time index
    daily_precip = precip[i, :, :]  # Assuming 2D precipitation data for each time step

    # Mask invalid values (e.g., large numbers or specific fill values)
    masked_precip = np.ma.masked_equal(daily_precip, 9.969209968386869e+36)  # Example of a fill value

    # Print masked precipitation data
    print(masked_precip)

# Close the dataset
f.close()
