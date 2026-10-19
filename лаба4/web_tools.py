import validators
from colorama import Fore

def check_url():
    url = input("\nВведіть адресу сайту: ")
    if validators.url(url):
        print(Fore.GREEN + "Адреса правильна.")
    else:
        print(Fore.RED + "Адреса неправильна.")
