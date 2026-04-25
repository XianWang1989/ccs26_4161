
for x in range(0, len(times)):
    loc = times.pop(0)
    if loc:  # Ensure loc is not empty
        rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
