from termcolor import RESET

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"


def red(msg):
    return f"{RED}{msg}{RESET}"

def green(msg):
    return f"{GREEN}{msg}{RESET}"

def yellow(msg):
    return f"{YELLOW}{msg}{RESET}"

