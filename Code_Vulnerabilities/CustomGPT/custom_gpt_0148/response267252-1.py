
ret = self.create_rrd(self.interval)
if ret:
    print("Error creating RRD file:", ret)
