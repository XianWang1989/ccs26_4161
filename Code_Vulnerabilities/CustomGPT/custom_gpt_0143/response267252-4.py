
def graph(self):
    ret = rrdtool.graph(
        "%s.png" % self.rrdfile,
        "--start", "-1h",  # Display data for the last hour
        "--vertical-label=ms",
        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
        "LINE:inoctets#7113D6:In Traffic",
        "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf ms",
        "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf ms"
    )
    if ret:
        print("Error generating graph:", ret)
