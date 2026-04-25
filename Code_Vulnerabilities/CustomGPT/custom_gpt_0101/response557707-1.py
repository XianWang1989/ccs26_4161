
import arcpy
import numpy
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# Dimensions and variables
lon = numpy.array(f.variables['lon'][:])
lat = numpy.array(f.variables['lat'][:])
time = numpy.array(f.variables['time'][:])
precip = numpy.array(f.variables['pre'][:])

# Output precipitation for each year
for i in range(len(time)):
    print("Precipitation for year:", time[i])
    # Ensure that you're using the correct index for precip
    # Handle possible invalid values
    valid_precip = precip[i][precip[i] != 9.969209968386869e+36]

    if valid_precip.size > 0:
        print(valid_precip)
    else:
        print("No valid precipitation data for this year.")
