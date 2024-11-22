from colorama import Fore

def rojo(mensaje:str)->str:
    return(Fore.RED + mensaje + Fore.RESET)

def verde(mensaje:str)->str:
    return(Fore.GREEN + mensaje + Fore.RESET)

def amarillo(mensaje:str)->str:
    return(Fore.YELLOW + mensaje + Fore.RESET)

def azul(mensaje:str)->str:
    return(Fore.BLUE + mensaje + Fore.RESET)
