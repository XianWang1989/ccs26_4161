
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read the dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Define the fill value (replace with the actual fill value if different)
fill_value = f.variables['pre'].missing_value

# Loop through each time index and print precipitation
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extract the precipitation data for the current time index
    precip_data = precip[i, :, :]

    # Mask the fill values
    masked_precip = np.where(precip_data == fill_value, np.nan, precip_data)

    # Print the masked precipitation data
    print(masked_precip)

# Close the dataset
f.close()
