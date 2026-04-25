
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Assuming -9999.0 is the missing value, you may need to check your dataset for the correct value
missing_value = -9999.0

# Loop through time indices and extract precipitation
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    annual_precip = precip[i, :, :]  # Adjust the indexing based on your netCDF structure

    # Masking the missing values
    masked_precip = np.ma.masked_where(annual_precip == missing_value, annual_precip)

    print(masked_precip)
