
import re
import asyncio
import aiofiles

async def process_log_line(log_line, conf, date_string):
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
        # Print the line asynchronously
        print(log_line.strip())

async def main():
    conf = {
        # Your configuration dictionary here
        'key1': ['pattern1', 'pattern2'],
        'key2': ['pattern3']
    }
    date_string = '2023-07-03 '  # Example date string

    async with aiofiles.open("file.txt", mode='r') as log_file:
        async for log_line in log_file:
            await process_log_line(log_line, conf, date_string)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
