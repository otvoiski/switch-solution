import six

from pyfiglet import figlet_format
from clint.textui import puts, colored, indent


try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def printColorInline(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color), end='')
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)


def printColor(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)


def getLogging():
    """
        console.log("This is a log.")
        console.error("This is an error.")
        console.info("This is some neutral info.")
        console.success("This is a success message.")

        # If using the new usage:
        console.setVerbosity(4) # verbosity from 1 - 5, in order:

        [1] Errors
        [2] Successes
        [3] Logs
        [4] Info
        [5] Secure

        console.mute() # shorthand for setVerbosity(0)
    """
    from console_logging.console import Console
    console = Console()
    console.setVerbosity(2)
    console.log("This should show up as a log.")
    console.error("This should show up as an error.")
    console.success("This should show up as a success.")
    console.info("This should show up as an info.")
    console.secure("Test", "This should not show up.")

    console.log("This should show up as a log.")
    console.error("This should show up as an error.")
    console.success("This should show up as a success.")
    console.info("This should show up as an info.")
    console.secure("Test", "This should show up.")
