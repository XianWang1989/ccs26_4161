
def graph(self, mins):
    # Check if the RRD file exists
    if not os.path.isfile(self.rrdfile):
        print(f"Error: {self.rrdfile} does not exist. Please create it first.")
        return

    ret = rrdtool.graph(f"{self.rrdfile}.png",
                        "--start", "-1",
                        "--end", "+1",
                        "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "COMMENT:  ",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")

    # Check for errors in graph generation
    if ret is None:
        print(f"Graph generation failed: {rrdtool.error()}")
    else:
        print("Graph generated successfully.")
