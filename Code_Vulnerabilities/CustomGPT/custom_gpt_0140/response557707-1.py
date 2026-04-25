
import arcpy
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Get variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])
fill_value = f.variables['pre']._FillValue  # Get the fill value

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for:", time[i])

    # Extract precipitation for the specific time index
    yearly_precip = precip[i]

    # Replace fill values with NaN
    yearly_precip = np.where(yearly_precip == fill_value, np.nan, yearly_precip)

    # Print non-repeating precipitation values
    print(yearly_precip[~np.isnan(yearly_precip)])  # Only print valid values
