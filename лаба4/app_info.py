from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

def show_info():
    print(Fore.GREEN + "Лабораторна робота №4")
    print("Робота з бібліотеками Python")
    print("Дата:", datetime.now().strftime("%d.%m.%Y"))
