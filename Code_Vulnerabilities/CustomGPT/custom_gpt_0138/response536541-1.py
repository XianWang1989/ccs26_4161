
import re
import asyncio

async def process_log_line(LogLine, Conf, DateString):
    flag = True
    for key, ConfLine in Conf.items():
        for patterns in ConfLine:
            patterns = DateString + patterns
            if re.match(patterns, LogLine):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(LogLine.strip())

async def main():
    with open("file.txt") as Log:
        tasks = []
        DateString = "your_date_format_here"  # Replace with your date format
        Conf = {
            # Your dictionary configuration here
        }
        for LogLine in Log:
            tasks.append(process_log_line(LogLine, Conf, DateString))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
