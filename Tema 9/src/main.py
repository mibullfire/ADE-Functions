from funciones import *

# Para impresión de cuadro de amortización con cuotas constantes, modificar estos datos:
inversion = 100000
tae = 0.1
ciclos_n = 4
impresion(cuadro_amortizacion(inversion, tae, ciclos_n))

# Para calcular tae en otros periodos:
tae = 0.06837
tipo_original = 'bimestral' # mensual/trimestral/semestral/anual
tipo_nuevo = 'anual' # mensual/trimestral/semestral/anual
#print(cambio_tae(tae, tipo_original, tipo_nuevo))

#print(calc_ank(0.05, 3))