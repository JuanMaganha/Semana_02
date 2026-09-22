# Vamos a crear una variable
monto = 123.45
alumno = "Javier"
edad = 21
aprobado = True

"""
variable = 1
print(type(variable))
variable = 12.56
print(type(variable))
variable = "dos"
print(type(variable))
variable = False
print(type(variable))
"""
"""
deudor = "Alvin"
monto_deuda = 500
pendiente_deuda = False
saldo_actual = monto_deuda * pendiente_deuda
print(saldo_actual)
"""
"""
compras_semana = 0
cantidad_compras = 0

compra_lunes = 100
compras_semana += compra_lunes
cantidad_compras += 1
compra_martes = 200
compras_semana += compra_martes
cantidad_compras += 1
compra_miercoles = 300
compras_semana += compra_miercoles
cantidad_compras += 1
compra_jueves = 400
compras_semana += compra_jueves 
cantidad_compras += 1
compra_viernes = 500
compras_semana += compra_viernes 
cantidad_compras += 1
print(compras_semana)
print(cantidad_compras)
"""

comprador = "Johny"
vendedor = "Carlitos"
compra = 25
compra_con_impuestos = comprador * 2
#print(compra_con_impuestos)
#print( comprador + " le compro a " + vendedor)
print(f"{comprador} le compro a {vendedor} la cantidad de {round (compra * 1.10,2)}")
round (12.65466,2)