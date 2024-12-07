from colorama import Fore

def rojo(mensaje:str)->str:
    print(Fore.RED + mensaje + Fore.RESET)

def verde(mensaje:str)->str:
    print(Fore.GREEN + mensaje + Fore.RESET)

def amarillo(mensaje:str)->str:
    print(Fore.YELLOW + mensaje + Fore.RESET)

def azul(mensaje:str)->str:
    print(Fore.BLUE + mensaje + Fore.RESET)
