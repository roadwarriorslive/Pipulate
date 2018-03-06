from logzero import logger, setup_logger
import schedule as sched
from pyfiglet import figlet_format
from colorama import Fore

font = 'standard'
subfont = 'cybermedium'
green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE

ascii_art1 = figlet_format('Hello World', font=font)
ascii_art2 = figlet_format('The red pill is a good choice', font=subfont)
print('%s%s%s' % (green, ascii_art1, white))
print('%s%s%s' % (red, ascii_art2, white))
