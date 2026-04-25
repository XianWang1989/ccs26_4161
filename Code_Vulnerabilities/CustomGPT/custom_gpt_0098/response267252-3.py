
def _doPing(self, host):
    for x in range(self.probes):
        result = subprocess.run(
            ["ping", "-c", "3", "-w", "6", host],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            rtt_line = [line for line in result.stdout.splitlines() if "rtt" in line][0]
            latency = rtt_line.split('/')[4]
            self.rrdList.append(latency)
        else:
            print(f"Ping failed for {host}.")
        time.sleep(1)  # Pause between pings
    return self.rrdList
