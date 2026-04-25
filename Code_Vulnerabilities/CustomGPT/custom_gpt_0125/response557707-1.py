
import arcpy
import numpy as np
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:], dtype=np.float32)  # Adjust dtype as necessary

# Loop through time and print valid precipitation values
for i in range(len(time)):
    print("Precipitation for:", time[i])
    # Check for valid precipitation values
    valid_precip = precip[i][np.isfinite(precip[i])]  # Only print finite values
    if valid_precip.size > 0:
        print(valid_precip)
    else:
        print("No valid precipitation data available for this time step.")
