
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Read dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=np.float32)  # Ensure the correct dtype

# Masking invalid precipitation values
# Assuming the invalid value is 9.969209968386869e+36, you can use np.ma.masked_equal
masked_precip = np.ma.masked_equal(precip, 9.969209968386869e+36)

for i in range(len(time)):
    print("Precipitation for year:", time[i])

    # Get precipitation data for the specific time index
    daily_precip = masked_precip[i, :, :]  # Adjust indexing as needed based on your data dimensions

    # Process only valid precipitation values
    if np.ma.is_masked(daily_precip):
        print("Valid precipitation values:")
        print(daily_precip.compressed())  # Display non-masked values
    else:
        print("No valid precipitation data available for this year.")
