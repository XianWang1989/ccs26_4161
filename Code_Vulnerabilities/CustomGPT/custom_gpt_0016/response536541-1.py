
import re
import asyncio

async def async_print(line):
    print(line.strip())

async def process_logs(log_file, conf):
    with open(log_file) as log:
        for log_line in log:
            # Assume `DateString` is defined elsewhere in your code
            patterns = [DateString + pattern for patterns in conf.values() for pattern in patterns]
            flag = True
            for pattern in patterns:
                if re.match(pattern, log_line):
                    flag = False
                    break
            if flag:
                await async_print(log_line)

if __name__ == '__main__':
    Conf = {
        "key1": ["pattern1", "pattern2"],
        "key2": ["pattern3"]
    }
    DateString = "2023-03-15"  # Example date string
    asyncio.run(process_logs("file.txt", Conf))
