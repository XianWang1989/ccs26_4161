
import subprocess

def _doPing(self, host):
    for _ in range(self.probes):
        try:
            result = subprocess.check_output(
                ["ping", "-c", "3", "-w", "6", host],
                universal_newlines=True
            )
            # Extracting RTT
            rtt_line = [line for line in result.splitlines() if "rtt" in line]
            if rtt_line:
                rtt = rtt_line[0].split('/')[-3]  # Get the average RTT
                self.rrdList.append(float(rtt))
            else:
                print(f"No RTT data found for {host}")
                self.rrdList.append(None)  # Append None if there’s no data

        except subprocess.CalledProcessError as e:
            print(f"Ping failed for {host}: {e}")
            self.rrdList.append(None)  # Append None on failure

    return self.rrdList
