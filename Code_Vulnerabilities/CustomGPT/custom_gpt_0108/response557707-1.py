
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Read dimensions and variables from the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Adjust dtype as needed

# Get the fill value (often this is -9999 or another specific value)
fill_value = f.variables['pre']._FillValue if '_FillValue' in f.variables['pre'].ncattrs() else np.nan

# Iterate over time and print precipitation, masking the fill values
for i, t in enumerate(time):
    print("Precipitation for:", t)
    precip_data = precip[i, :, :]  # Assuming precip is time x lat x lon
    precip_masked = np.ma.masked_equal(precip_data, fill_value)
    print(precip_masked)
