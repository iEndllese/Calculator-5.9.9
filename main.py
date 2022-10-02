#--------------------------------------------
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from os import system as os
init(autoreset = False)
#--------------------------------------------

#--------------------------------------------
C = Fore.CYAN + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
R = Fore.RED + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
B = Fore.BLACK + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
#--------------------------------------------

#--------------------------------------------
Script_Tegs = G + figlet_format("calculator", font="cybermedium")
version = B + "\t\t\t\tversion 5.9.9"
print(Script_Tegs, version)
#--------------------------------------------

#--------------------------------------------
while True:
	
	try:
		x = eval(input(C + "\nMethod: " + W))
		print(C + f"Итого: {W} {x}")
		
	except Exception as error:
		exec('os("cls || clear")') 
		exec('print(Script_Tegs, version)')
		print(Y + f"\nНеправильно введены данные!")
		print(f"Ошибка: {R}{error}")
#--------------------------------------------
