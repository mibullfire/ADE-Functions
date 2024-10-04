# Valores
valor_inicial = 18000
v0 = valor_inicial
valor_residual = 800
n = 20
t = round(1 - (valor_residual/valor_inicial)**(1/n), 4)

# Operaciones
print(f'Valor Inicial: {valor_inicial}')
print(f'Valor Residual: {valor_residual}')
print(f'Años: {n}')
print(f'El tanto es: {t}.')

print('\nTabla\n')

print(f'Año 0  //  A0 = 0  //  Vo = {valor_inicial}')
for i in range (1,n+1):
    a = round(t * valor_inicial, 4)
    valor_inicial = valor_inicial - a
    print(f'Año {i}  //  A{i} = {a}  //  Q{i} = {valor_inicial}')

print(f'\nÚltima cuota = {round(a, 0)} y Valor Residual = {round(valor_inicial, 0)}')

print(f'\nPor el método del tanto fijo, la cuota constante = {(v0-valor_residual)/n}.\n')