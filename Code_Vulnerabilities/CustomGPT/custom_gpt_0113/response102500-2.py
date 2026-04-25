
if __name__ == '__main__':
    LOG_FILENAME = '/home/me/logs/mylog.txt'
    file_handler = logging.FileHandler(LOG_FILENAME)
    logging.getLogger().addHandler(file_handler)
