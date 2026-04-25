
import logging

logging.basicConfig(level=logging.DEBUG)
db._adapter.extra_params['charset'] = 'utf8mb4'  # Ensure the character set is appropriate
