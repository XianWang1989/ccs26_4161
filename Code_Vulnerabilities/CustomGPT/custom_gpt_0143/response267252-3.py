
for loc in self.rrdList:
    update_status = rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(loc)))
    if update_status:
        print("Error updating RRD:", update_status)
