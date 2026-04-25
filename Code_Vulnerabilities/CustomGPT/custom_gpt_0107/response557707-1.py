
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Ensure the correct variable

# Loop through the time variable
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Fetch precipitation for the specific time index
    current_precip = precip[i, :, :]  # Assuming precip has dimensions (time, lat, lon)

    # Mask the large fill value (if necessary)
    current_precip[current_precip == 9.969209968386869e+36] = np.nan

    # Print the precipitation array for the current year
    print(current_precip)

# Close the NetCDF file
f.close()
