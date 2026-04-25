
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='netCDF4')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming the fill value is 9.969209968386869e+36
fill_value = 9.969209968386869e+36

# Loop through each time index
for i in range(len(time)):
    current_precip = precip[i]
    # Mask fill values
    current_precip_masked = np.ma.masked_where(current_precip == fill_value, current_precip)

    # Check if there are valid precipitation values
    if current_precip_masked.count() > 0:
        print("Precipitation for year:", time[i])
        print(current_precip_masked)
    else:
        print("No valid precipitation data for year:", time[i])

# Close the dataset
f.close()
