from collections import namedtuple
from colorama import Fore
from tabulate import tabulate
import pandas as pd

def tabla(valor_inicial,v0,valor_residual,n,decimales_t)->None:

    t = round(1 - (valor_residual/valor_inicial)**(1/n), decimales_t)
    #t=0.1
    # Presentación de los valores
    print(f'Valor Inicial: {valor_inicial}')
    print(f'Valor Residual: {valor_residual}')
    print(f'Años: {n}')
    print(f'El tanto es: {t}.')

    # Operaciones
    calculo_anyo = namedtuple('Año', 'Año, Ai, Qi')
    lista = []
    lista.append(calculo_anyo(0, 0, v0))
    for i in range (1,n+1):
        a = round(t * valor_inicial, 4)
        valor_inicial = valor_inicial - a
        lista.append(calculo_anyo(i, a, valor_inicial))

    datos = [[i.Año, i.Ai, i.Qi] for i in lista]
    
    # Crear DataFrame con los datos
    columnas = ["Año", "Ai", "Qi"]
    df = pd.DataFrame(datos, columns=columnas)
    # Usar tabulate para mostrar la tabla en la terminal
    print(Fore.RED+'\nTabla de Cuadro de Amortización\n'+Fore.BLUE)
    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
    print(f'\nÚltima cuota = {round(a, 0)} y Valor Residual = {round(valor_inicial, 0)}')
    print(Fore.GREEN + f'\nPor el método del tanto fijo, la cuota constante = {(v0-valor_residual)/n}.\n' + Fore.RESET)

# Valores
valor_inicial = 400000
v0 = valor_inicial
valor_residual = 50000
n = 4
decimales_t = 6 # Número de decimales de la tasa del tanto fijo 
tabla(valor_inicial, v0, valor_residual, n, decimales_t)