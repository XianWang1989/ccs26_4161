
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Get variables: dimensions and precipitation data
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre'][:]  # Precipitation data

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for index", i, ":", time[i])

    # Use the correct index to extract the corresponding precip data
    current_precip = precip[i, :, :]  # Assuming precip is 3D (time, lat, lon)

    # Print the current precipitation array
    print(current_precip)

# Don't forget to close the file when done
f.close()
