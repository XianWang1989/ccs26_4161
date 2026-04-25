
import numpy as np
import netCDF4 as nc

# Load the netCDF file
f = nc.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjust dtype if needed

# Check for valid values and handle the placeholder
valid_precip = np.where(precip != 9.969209968386869e+36, precip, np.nan)  # Replace with NaN

# Loop through time and output precipitation values
for i in range(len(time)):
    print(f"Precipitation for year {time[i]}:", valid_precip[i])

# Close the dataset
f.close()
