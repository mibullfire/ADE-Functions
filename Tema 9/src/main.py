from funciones import *

# Para impresión de cuadro de amortización con cuotas constantes, modificar estos datos:
inversion = 600000
tae = 0.02
ciclos_n = 4
# impresion(cuadro_amortizacion(inversion, tae, ciclos_n))

# Para calcular tae en otros periodos:
tae = 0.02
tipo_original = 'anual' # mensual/trimestral/semestral/anual
tipo_nuevo = 'mensual' # mensual/trimestral/semestral/anual
print(cambio_tae(tae, tipo_original, tipo_nuevo))