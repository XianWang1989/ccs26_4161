
for loc in self.rrdList:
    if loc:
        rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
