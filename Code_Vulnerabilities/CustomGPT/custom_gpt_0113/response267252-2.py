
import rrdtool

# Create an RRD file with dummy data
rrdtool.create("test.rrd", "--step", "300",
                "DS:dummy:GAUGE:600:0:U",
                "RRA:AVERAGE:0.5:1:288")

# Update it with some dummy values
for i in range(10):
    rrdtool.update("test.rrd", f"N:{i}")

# Graph the data
rrdtool.graph("test.png",
              "--start", "-1h",
              "DEF:dummy=test.rrd:dummy:AVERAGE",
              "LINE:dummy#00FF00:Dummy Data")
