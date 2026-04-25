
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the missing value (fill value)
missing_value = f.variables['pre']._FillValue  # Adjust depending on how it’s set in your file

# Loop through time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for year index:", i)
    yearly_precip = precip[i]

    # Remove invalid values (fill values)
    valid_precip = np.ma.masked_equal(yearly_precip, missing_value)

    print(valid_precip)
