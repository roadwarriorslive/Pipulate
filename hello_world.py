from logzero import logger, setup_logger
import schedule as sched
from pyfiglet import figlet_format
from colorama import Fore

font = 'standard'
green = Fore.GREEN
white = Fore.WHITE

ascii_art1 = figlet_format('Hello World', font=font)
print('%s%s%s' % (green, ascii_art1, white))
