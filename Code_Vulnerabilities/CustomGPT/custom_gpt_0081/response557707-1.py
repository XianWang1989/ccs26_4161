
import numpy as np
import netCDF4

# Open the NetCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Check the fill value; common fill value for many datasets is 9.969209968386869e+36
fill_value = 9.969209968386869e+36  

# Replace the fill values with NaN
precip[precip == fill_value] = np.nan

# Loop through each time index and print precipitation values
for i in range(len(time)):
    print("Precipitation for year index:", i)
    # Get the precipitation data for that specific time index
    precip_values = precip[i, :, :]  # Adjust based on your variable's dimensions
    # Optionally replace NaNs with zeros, or handle them as per your requirements
    precip_values = np.nan_to_num(precip_values, nan=0.0)

    # Print the values
    print(precip_values)

# Close the dataset once done
f.close()
