costes_fijos = 220000000
p = 150000 # Coste de cada equipo
n = 4800
coste_variable = 125500

#Punto Muerto
m = p - coste_variable
qo = costes_fijos/m
print('Punto Muerto')
print(f'Coste Fijo = {costes_fijos}\nm = p - cv = {p} - {coste_variable} = {m}\nPunto Muerto = CF / m = {costes_fijos} / {m} = {qo}\n')

#Apalancamiento
#n = 4800 # Variable
ao = round(n/(n - qo), 2)
print('Apalancamiento')
print(f'El Apalancamiento es Ao = Q / (Q - Qo) = {n} / {n - qo} = {ao}\n')

#Margen de Seguridad
#n = 4800 # Variable
ms = p * (n - qo)
print('Margen de Seguridad')
print(f'El Margen de Seguridad es MS = p x (Q - Qo) = {p} x ({n} - {qo}) = {ms}\n')

#Beneficios
print('Beneficios Anuales')
print(f'Los Beneficios Anuales son: B = m x n - CF = {m} x {n} - {costes_fijos} = {m*n-costes_fijos}\n')