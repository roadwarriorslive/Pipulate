from logzero import logger, setup_logger
import schedule as sched
from pyfiglet import figlet_format
from colorama import Fore
font, subfont = 'standard', 'cybermedium'
green, red, white = Fore.GREEN, Fore.RED, Fore.WHITE
ascii_art1 = figlet_format('Begin Tracking', font=font)
print('%s%s%s' % (green, ascii_art1, white))
