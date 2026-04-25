
ret = rrdtool.create("...", ...)
if ret is None:
    print("Error creating RRD file:", rrdtool.error())
