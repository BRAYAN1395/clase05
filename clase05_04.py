# ----------------------------------------------------------
# Boleta de pago de tienda
# Si se vende mas de 10 unidades se aplicara un descto de 5%
# ----------------------------------------------------------
print('-----------')
print('Bodega Mass')
print('-----------')
xcambio = 3.4
xvendedor = 'Juan Alva'
xpro = input('Ingrese producto : ')
xpre = float(input('Ingrese precio : '))
xcan = int(input ('Ingrese cantidad : '))

if(xcan >10):
    # Hay descto 5%
    xdescto = 0.05
else:
    #No hay descto
    xdescto = 0
#Calcular el importe a pagar        

ximporte = xcan * xpre - xdescto * xcan * xpre
#Mostrar resultados
print('El descuento es : ', xdescto * xcan * xpre)
print('total a pagar S/: ', ximporte)
print('total a pagar US/: ', round (ximporte/xcambio,2))
print('************************************************')
xpago = float(input('ingrese pago :'))
xmoneda = input('Moneda (S) o (D) :')
if(xmoneda.upper =='S'):
    print('El vuelto :', round(xpago - ximporte,2))
else:
    xsoles = xpago / xcambio # Convertis a soles
    print('El vuelto :', round(xsoles - ximporte,2))
print('************************************************')
print('Comision del vendedor')
print('La comision es :', 0.02*ximporte)