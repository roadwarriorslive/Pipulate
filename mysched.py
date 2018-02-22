import schedule as sched
from pyfiglet import figlet_format
from colorama import Fore
from logzero import logger, setup_logger

UTCRebootTime = '06:00' # Generally, 1-AM for me
beat_count = 0
font = 'standard'
subfont = 'cybermedium'
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE

ascii_art1 = figlet_format('Congratulations!', font=font)
ascii_art2 = figlet_format('Welcome to Wonderland.!', font=subfont)
print('%s%s%s' % (green, ascii_art1, white))
print('%s%s%s' % (blue, ascii_art2, white))

logger = setup_logger(logfile='mysched.log', maxBytes=1000000, backupCount=3)
logger.info('This is some logger info.')
