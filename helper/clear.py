import os
from .banner import banner

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_with_banner():
    clear()
    banner()
