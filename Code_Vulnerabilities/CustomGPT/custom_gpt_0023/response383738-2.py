
def announce(inputurl):
    try:
        with urllib.request.urlopen(inputurl) as url:
            response = url.read()
            print("Raw response:", response)

            decoded = bdecode(response)
            print("Decoded response:", decoded)
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
