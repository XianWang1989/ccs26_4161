
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    for _ in range(self.probes):  # Fixed range loop
        loc = self._doPing(host)
        if loc:  # Check if loc is not empty
            try:
                value = int(float(loc[0]))  # Get first value safely
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{value}')
                print(f'{int(time.time())}:{value}')
            except ValueError:
                print("Error: Non-numeric value returned from ping.")
        time.sleep(5)
    self.graph(60)

def graph(self, mins):
    try:
        ret = rrdtool.graph(f"{self.rrdfile}.png", 
                            "--start", f"-{mins * 60}",
                            "--vertical-label=Packets",
                            f"DEF:packets={self.rrdfile}:packets:AVERAGE",
                            "AREA:packets#7113D6:In traffic",
                            "CDEF:inbits=packets,8,*",
                            "COMMENT:\\n",
                            "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                            "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    except Exception as e:
        print(f"Graphing error: {e}")
