
import asyncio
import re

async def process_log(log_line, conf):
    flag = True
    for key, conf_line in conf.items():
        for pattern in conf_line:
            full_pattern = date_string + pattern
            if re.match(full_pattern, log_line):
                flag = False
                break
        if not flag:
            break
    if flag:
        await print_async(log_line.strip())

async def print_async(message):
    print(message)

async def main():
    date_string = "2023-01-01"  # Example date string
    conf = {
        "example_key": ["pattern1", "pattern2"]
    }

    with open("file.txt") as log:
        tasks = []
        for log_line in log:
            tasks.append(process_log(log_line, conf))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
