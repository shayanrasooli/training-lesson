from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.GREEN + "Your are welcome")
print(Fore.YELLOW + "This is a warning message.")


print(Fore.RED + "This is an error message.")

print(Back.BLUE + "This text has a blue background.")

print(Style.BRIGHT + Fore.CYAN + "Welcome to Python Training!")