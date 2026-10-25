#Operadores Aritmeticos

print("Operadores")

print("Operadores Aritmeticos")

print("+ Suma: ", 5, "+", 3, "=", 5+3)
print("- Resta: ", 5, "-", 3, "=", 5-3)
print("* Multiplicacion: ", 5, "*", 3, "=", 5*3)
print("/ Division: ", 5, "/", 3, "=", 5/3)
print("// Division Entera: ", 5, "/", 3, "=", 5/3)
print("% Residuo: ", 10, "%", 3, "=", 5%3)
print("** Potencia: ", 5, "**", 3, "=", 5**3)


print ("Tabla de multiplicar del 5")
print (5, "*", 1, "=", 5*1)
print (5, "*", 1, "=", 5*2)
print (5, "*", 1, "=", 5*3)
print (5, "*", 1, "=", 5*4)
print (5, "*", 1, "=", 5*5)
print (5, "*", 1, "=", 5*6)
print (5, "*", 1, "=", 5*7)
print (5, "*", 1, "=", 5*8)
print (5, "*", 1, "=", 5*9)
print (5, "*", 1, "=", 5*10)

print(" OPERADORES DE COMPARACION  ")

print("== Igual a:", 5, "==", 5, 5==5)
print("== Igual a:", 5, "==", 4, 5==4)
print("!= Igual a:", 5, "==", 4, 5!=4)
print("!= Igual a:", 5, "!=", 5, 5!=5)
print("> Mayor que:", 5, ">", 5, 5>5)
print("> Mayor que:", 5, ">", 5, 5>5)
print("< Menor que:", 5, "<", 5, 5<5)
print("< Menor que:", 5, "<", 5, 5<5)
print(">= Mayor o igual que:", 5, ">=", 5, 5>=5)
print(">= Mayor o igual que:", 5, ">=", 5, 5>=5)
print("<= Menor o igual que:", 5, "<=", 5, 5<=5)
print("<= Menor o igual que:", 5, "<=", 5, 5<=5)

print("OPERADORES LÓGICAS")
print("Operador and: (5==5) and (4>3)", (5==5)and(4>3))
print("Operador and: (5==5) and (4>3)", (5==5)and(4>8))
print("Operador or: (5==5) or (4>3)", (5==5)or(4>8))
print("Operador or: (5==5) or (4>3)", (5==6)or(4>8))
print("Operador and: not (5==6)", not (5==6))
print("Operador and: not (5==5)", not (5==5))

tiene_dinero = True
tienda_abierta = True

puede_comprar = tiene_dinero and tienda_abierta
print("¿Puede comprar?", puede_comprar)

es_cliente_vip = True
tiene_dinero = False
acceso_credito = es_cliente_vip or tiene_dinero
print("¿Crédito aprobado?", acceso_credito)
