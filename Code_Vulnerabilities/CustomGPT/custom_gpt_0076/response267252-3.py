
ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep 'rtt' | awk -F '/' '{print $5}'" % host)
if ans != 0:
    print("Ping failed:", unans)
    return None
