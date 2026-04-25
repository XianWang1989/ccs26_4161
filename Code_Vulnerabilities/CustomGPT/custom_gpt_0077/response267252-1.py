
def graph(self, mins):
    try:
        ret = rrdtool.graph("%s.png" % self.rrdfile,
                            "--start", "-%d" % mins,
                            "--end", "now",
                            "--step", "300",
                            "--vertical-label=Packets",
                            "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                            "AREA:packets#FF0000:Packets",
                            "GPRINT:packets:AVERAGE:Avg Packets\: %6.2lf",
                            "GPRINT:packets:MAX:Max Packets\: %6.2lf",
                            "COMMENT:\\n")

        if ret:
            print("Graph creation failed:", ret)
        else:
            print("Graph created successfully.")

    except Exception as e:
        print(f"An error occurred while generating the graph: {e}")
