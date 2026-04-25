
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Load variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming the time dimension is the first index, adjust if necessary
for i in range(len(time)):
    print("Year:", time[i])

    # Access precipitation data for the current time index
    precip_data = precip[i, :, :]  # Adjust dimensions as needed

    # Masking invalid values
    precip_data[precip_data == 9.969209968386869e+36] = np.nan

    # Print valid precipitation values
    print("Precipitation data:", precip_data)

# Close the dataset
f.close()
