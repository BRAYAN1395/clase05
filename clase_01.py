#clase
# TRAPECIO
# AUTOR : BRAYAN LOPEZ MUJICA
# Fecha : 29-10-2024
# ---------------------------------
# 1. Cabecera
print('-----------------')
print('Area del trapecio')
print('-----------------')
# 2. Ingreso de datos
xbmayor = int( input('ingrese base mayor : '))
xbmenor = int( input('ingrese base menor : '))
xaltura = int( input('ingrese la altura : '))
# 3. validar
if (xbmayor < xbmenor):
    print('Verificar datos de las bases ingresadas')
else:
    #4. Proceso
    xarea = (xbmayor + xbmenor) / 2
    #5. Resultados
    print('El area del trapecio es : ', xarea)