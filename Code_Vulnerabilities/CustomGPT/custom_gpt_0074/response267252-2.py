
def create_rrd(self, interval):
    ret = rrdtool.create(...)

    if ret:
        print("Failed to create RRD file:", ret)
    else:
        print("RRD file created successfully.")
