
import logging
import os

logging.basicConfig(
    filename='/path/to/logs/test.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

logging.debug("Debug message from test script!")
