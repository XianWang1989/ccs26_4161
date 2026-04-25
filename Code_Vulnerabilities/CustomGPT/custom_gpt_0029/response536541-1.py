
import re
import concurrent.futures

def process_line(LogLine, Conf, DateString):
    flag = True
    for key, ConfLine in Conf.items():
        for pattern in ConfLine:
            full_pattern = DateString + pattern
            if re.match(full_pattern, LogLine):
                return None  # Skip printing if a match is found
    return LogLine.strip()  # Return the line if no match

def main():
    DateString = "your_date_string_here"  # Adjust as necessary
    Conf = {'example_key': ['pattern1', 'pattern2']}  # Your config dictionary

    with open("file.txt") as Log:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Process lines concurrently
            futures = {executor.submit(process_line, line, Conf, DateString): line for line in Log}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    print(result)

if __name__ == "__main__":
    main()
