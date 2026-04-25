
import arcpy
import numpy
import netCDF4

# Load the netCDF file
f = netCDF4.Dataset('Y:\\Projects\\ToriW\\NC Files\\TP40Years.nc', 'r', format='NetCDF4')

# The dimensions and variables of the netCDF file
lon = numpy.array(f.variables['lon'][:])
lat = numpy.array(f.variables['lat'][:])
time = numpy.array(f.variables['time'][:])
precip = numpy.array(f.variables['pre'][:])

# Get the fill value (usually looks like 9.969209968386869e+36)
fill_value = f.variables['pre']._FillValue

# Loop through each time index
for t in range(len(time)):
    # Mask out the fill values in the precipitation data
    precip_masked = numpy.ma.masked_equal(precip[t, :, :], fill_value)

    # Print the year or time associated with the data
    print("Precipitation for year:", time[t])

    # Print the masked precipitation values
    print(precip_masked)
