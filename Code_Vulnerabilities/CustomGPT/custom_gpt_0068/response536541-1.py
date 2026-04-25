
import re

# Open your log file
Log = open("file.txt")

# Assuming `Conf` is defined somewhere in your script
results = []  # A list to hold lines to be printed
DateString = "YOUR_DATE_PATTERN_HERE" # Define your date pattern

for LogLine in Log:
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break 
        if not flag:  # breaks the outer loop if flag is False
            break 

    if flag:
        results.append(LogLine.strip())  # Store lines instead of printing immediately

# Close the log file to free up resources
Log.close()

# Print all results at once.
print("\n".join(results))
