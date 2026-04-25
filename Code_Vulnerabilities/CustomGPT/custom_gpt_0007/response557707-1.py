
import arcpy
import numpy
import netCDF4

# Open the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NETCDF4')

# Read dimensions and variables
lon = numpy.array(f.variables['lon'][:])
lat = numpy.array(f.variables['lat'][:])
time = numpy.array(f.variables['time'][:])
precip = numpy.array(f.variables['pre'][:])

# Loop through the time variable
for i in range(len(time)):
    print("Precipitation for time index:", i)
    print(precip[i])  # Access the data directly for each time step
