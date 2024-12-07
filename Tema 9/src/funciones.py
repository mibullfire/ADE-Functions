from collections import namedtuple
from tabulate import tabulate
import pandas as pd
from mensajes import *
from sympy import symbols, Eq, solve


amortizacion = namedtuple('Amortización', 'año, cuota, intereses, devolucion_principal, capital_pendiente')

def calc_ank(tae:float, año:int)->float:
    return (1-(1/(1+tae)**año))/(tae)

def calc_cuota(inversion:float, ank:float)->float:
    return inversion/ank

def cuadro_amortizacion(inversion:float, tae:float, año:int)->list[amortizacion]:
    ank = calc_ank(tae, año)
    cuota = calc_cuota(inversion, ank)
    lista = []
    lista.append(amortizacion(0, cuota, 0, 0, inversion))
    capital_pendiente_old = inversion
    for i in range(1, año+1):
        intereses = capital_pendiente_old * tae
        devolucion = cuota - intereses
        capital_pendiente_new = capital_pendiente_old - devolucion
        capital_pendiente_old = capital_pendiente_new
        lista.append(amortizacion(
            i,
            cuota,
            round(intereses, 2),
            round(devolucion, 2),
            round(capital_pendiente_new, 2)
        ))
    return lista

def impresion(lista:list[amortizacion])->None:
    datos = [[i.año, i.cuota, i.intereses, i.devolucion_principal, i.capital_pendiente] for i in lista]
    
    # Crear DataFrame con los datos
    columnas = ["Año", "Cuota", "Intereses", "Devolución", "Capital Pendiente"]
    df = pd.DataFrame(datos, columns=columnas)
    # Usar tabulate para mostrar la tabla en la terminal
    amarillo('Tabla de Cuadro de Amortización')
    azul(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

def tipos_exponentes(tipo:str)->float:
    match tipo:
        case 'mensual':
            return 12
        case 'bimestral':
            return 6
        case 'trimestral':
            return 4
        case 'semestral':
            return 2
        case 'anual':
            return 1
        case _:
            rojo(f'Tipo de periodo ({tipo}) no reconocido, usa mensual/trimestral/semestral/anual')
            return 0

def cambio_tae(tae:float, tipo_original:str, tipo_nuevo:str)->str:
    # Definir la variable
    x = symbols('x')
    exp1 = tipos_exponentes(tipo_original)
    exp2 = tipos_exponentes(tipo_nuevo)

    ecuacion = Eq((1+tae)**exp1, (1+x)**exp2)
    
    # Resolver la ecuación
    resultado = solve(ecuacion, x)
    # Filtrar solo la solución real y "bonita"
    resultado_real = [float(sol.evalf()) for sol in resultado if sol.is_real and sol > 0]
    if resultado_real:
        solucion_bonita = float(resultado_real[0])  # Primera solución real
        res = verde(f'La solución es: {solucion_bonita:.5f}')  # Mostrar con 5 decimales
    else:
        res = rojo('No se encontraron soluciones reales.')
    return res