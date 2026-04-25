
import subprocess

def test_ping(host):
    try:
        result = subprocess.check_output(
            ["ping", "-c", "3", host],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        print("Ping successful:")
        print(result)
    except subprocess.CalledProcessError as e:
        print("Ping failed:", e.output)

# Example usage:
test_ping("example.com")
