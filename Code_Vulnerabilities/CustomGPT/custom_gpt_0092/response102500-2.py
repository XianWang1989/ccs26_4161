
if __name__ == '__main__':
    LOG_FILENAME = '/home/me/logs/mylog.txt'
    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
