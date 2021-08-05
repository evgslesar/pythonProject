import logging
import requests

# logging.basicConfig()
logger = logging.getLogger('app_logger')
print(logger)


console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
# console_handler.setFormatter(f)
#
# utils_logger = logging.getLogger('app_logger.utils')
# utils_logger.setLevel('DEBUG')
#

def main():
    logger.debug('Hello')

if __name__ == '__main__':
    main()

