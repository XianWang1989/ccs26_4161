
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Loop through each time index properly
for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Access the precipitation data corresponding to the current time index
    precip_for_year = precip[i, :, :]  # Adjust based on how your precipitation data is structured (e.g., (time, lat, lon))

    # Optionally, you can flatten the array if needed, or just print as is
    print(precip_for_year)

# Close the dataset
f.close()
