
import arcpy
import numpy
import netCDF4

# Load the netCDF dataset
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Extract dimensions and variables
lon = numpy.array(f.variables['lon'][:])
lat = numpy.array(f.variables['lat'][:])
time = numpy.array(f.variables['time'][:])
precip = numpy.array(f.variables['pre'][:], dtype=float)

# Identify and replace the invalid value with NaN
invalid_value = 9.969209968386869e+36
precip[precip == invalid_value] = numpy.nan

# Loop through each time index
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    print(precip[i,:,:])  # Adjust indexing to match the shape of your data
