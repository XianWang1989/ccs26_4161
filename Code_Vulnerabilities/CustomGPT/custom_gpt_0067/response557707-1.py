
import numpy as np
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Extract dimensions and variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = np.array(f.variables['pre'][:])

# Get the missing value indicator (usually it's a specific number)
missing_value = f.variables['pre']._FillValue

# Loop through time and print precipitation values
for idx, t in enumerate(time):
    print(f"Precipitation for time index {idx}: {t}")

    # Select precipitation data for the current time index
    precip_values = precip[idx, :, :]

    # Replace missing values with NaN for better filtering
    precip_values = np.where(precip_values == missing_value, np.nan, precip_values)

    # Print values without the missing value
    if np.any(~np.isnan(precip_values)):
        print(precip_values)
    else:
        print("No valid precipitation data available.")
