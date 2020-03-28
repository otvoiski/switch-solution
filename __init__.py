import six
import colorama

# set logger for all
from logging42 import logger
from pyfiglet import figlet_format
from termcolor import colored


def setLogging(debug):
    if not debug:
        logger.remove()


def printColorInline(string, color, font="slant", figlet=False):
    six.print_(colored(string, color), end='')


def printFiglet(string, color, font="slant",):
    print(colored(figlet_format(string, font=font), color))

def printColor(string, color):
    print(colored(string, color))