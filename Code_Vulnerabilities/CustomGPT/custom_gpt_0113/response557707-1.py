
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=np.float32)  # Ensure appropriate dtype

# Identify the fill value
fill_value = f.variables['pre']._FillValue

# Loop through time and extract precipitation, ignoring fill values
for i in range(len(time)):
    precip_year = precip[i]
    # Mask out the fill values
    precip_year = np.ma.masked_equal(precip_year, fill_value)

    print(f"Precipitation for year {time[i]}:")
    print(precip_year.compressed())  # Print values without fill values
