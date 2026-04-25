
import numpy as np
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r')

# Extract the variables
lon = np.array(f.variables['lon'][:])
lat = np.array(f.variables['lat'][:])
time = np.array(f.variables['time'][:])
precip = f.variables['pre']  # Keep it as a dataset for indexing

# Loop through the time variable
for i in range(len(time)):
    print("Precipitation for year index:", i)
    precip_data = precip[i, :, :]  # Access 2D array for the specific time index

    # Replace fill value with NaN for better handling
    fill_value = precip._FillValue if '_FillValue' in precip.ncattrs() else None
    if fill_value is not None:
        precip_data[precip_data == fill_value] = np.nan

    print(precip_data)

# Close the dataset
f.close()
