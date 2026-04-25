
def graph(self, mins):
    rrdtool.graph(f"{self.rrdfile}.png",
                  "--start", f"-{mins * 60}",
                  "--vertical-label=ms",
                  "DEF:rtt=%s:packets:AVERAGE" % self.rrdfile,
                  "LINE2:rtt#FF0000:RTT",
                  "GPRINT:rtt:AVERAGE:Avg RTT: %6.2lf ms",
                  "GPRINT:rtt:MAX:Max RTT: %6.2lf ms",
                  "GPRINT:rtt:MIN:Min RTT: %6.2lf ms")
