import logging
import sys
logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('Logger initialized')

def get_logger():
    return logger