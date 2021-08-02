import logging
import requests

logging.basicConfig(level='DEBUG')
logger = logging.getLogger()

logging.getLogger('urllib3').setLevel('CRITICAL')
# for key in logging.Logger.manager.loggerDict:
#     print(key)

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')

    r = requests.get('https://www.google.ru')



if __name__ == '__main__':
    main('oleg')

