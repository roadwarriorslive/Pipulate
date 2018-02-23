import time
import importlib
from datetime import date, datetime, timedelta
from logzero import logger, setup_logger
import schedule as sched
from pyfiglet import figlet_format
from colorama import Fore

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

the_time = str(datetime.now().time())[:5]
logger = setup_logger(logfile='mysched.log', maxBytes=1000000, backupCount=3)
logger.info("We're not in Jupyter Notebook anymore. The time is %s." % the_time)


def main():
    sched.every(10).minutes.do(heartbeat)
    next_min = minute_adder(1).strftime('%H:%M')
    logger.info("When the clock strikes %s, down the rabbit hole with you!" % next_min)
    sched.every().day.at(next_min).do(the_queue)
    sched.every().day.at(UTCRebootTime).do(reboot)
    while True:
        sched.run_pending()
        time.sleep(1)


def do_main(name):
    mod = importlib.import_module(name)
    mod.main()


def do_it(name):
    mod = importlib.import_module(name)


def heartbeat():
    global beat_count
    beat_count += 1
    logger.info("Heartbeat %s at %s" % (beat_count, datetime.now()))


def the_queue():
    logger.info("This is a scheduled event. Jump! Down the rabbit hole...")


def reboot():
    logger.info("Rebooting system.")
    import subprocess
    p = subprocess.Popen(['sh', 'r.sh'], cwd='/home/ubuntu/pipulate/')


def minute_adder(minutes):
    the_time = datetime.now().time()
    today = date.today()
    beat = timedelta(minutes=minutes)
    return_value = datetime.combine(today, the_time) + beat
    return return_value


if __name__ == '__main__':
    main()
