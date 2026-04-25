
import numpy as np
import netCDF4 as nc

# Load the netCDF file
f = nc.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# The dimensions and variables of the netCDF file
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])  # Assuming 'pre' is the precipitation variable

# Check for a fill value (e.g., netCDF4 default fill value for floats)
fill_value = f.variables['pre']._FillValue

# Loop through each time index to get precipitation data
for i in range(len(time)):
    print("Precipitation for year index:", i)

    # Extract precipitation for the current time index
    yearly_precip = precip[i]

    # Replace fill values with NaN (if necessary)
    yearly_precip[yearly_precip == fill_value] = np.nan

    print(yearly_precip)

# Close the netCDF file
f.close()
