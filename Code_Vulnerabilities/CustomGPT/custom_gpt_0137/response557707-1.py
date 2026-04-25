
import arcpy
import numpy
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Get the dimensions and variables of the netCDF file
lon = numpy.array(f.variables['lon'][:])
lat = numpy.array(f.variables['lat'][:])
time = numpy.array(f.variables['time'][:])
precip = numpy.array(f.variables['pre'][:])

# Loop through the time dimension
for i in range(len(time)):
    print(f"Precipitation for year {time[i]}:")
    # Accessing precipitation data for the specific time index i
    precip_data = precip[i, :, :]  # Assuming precip is structured as (time, lat, lon)

    # Print the precipitation array for the specific time step
    print(precip_data)
