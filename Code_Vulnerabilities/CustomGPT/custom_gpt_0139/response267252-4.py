
import logging

logging.basicConfig(filename='ping_rrd.log', level=logging.DEBUG)

# Inside your methods, use logging like this
logging.debug(f"Pinging {host}")
