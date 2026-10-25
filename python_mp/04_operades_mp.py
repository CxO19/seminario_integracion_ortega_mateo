# Operadores Aritmeticos
print("Operadores")
print("Operadores Aritmeticos")
print("+ Suma: ", 120, "+", 30, "=", 120+30)
print("- Resta: ", 250, "-", 50, "=", 250-50)
print("* Multiplicacion: ", 150, "*", 2, "=", 150*2)
print("/ Division: ", 300, "/", 2, "=", 300/2)
print("// Division Entera: ", 300, "/", 2, "=", 300//2)
print("% Residuo: ", 100, "%", 30, "=", 100%30)
print("** Potencia: ", 2, "**", 3, "=", 2**3)

print("Calculo de tarifas por asientos")
print(150, "*", 1, "=", 150*1)
print(150, "*", 2, "=", 150*2)
print(150, "*", 3, "=", 150*3)
print(150, "*", 4, "=", 150*4)
print(150, "*", 5, "=", 150*5)
print(150, "*", 6, "=", 150*6)
print(150, "*", 7, "=", 150*7)
print(150, "*", 8, "=", 150*8)
print(150, "*", 9, "=", 150*9)
print(150, "*", 10, "=", 150*10)

print(" OPERADORES DE COMPARACION  ")
print("== Igual a:", 120, "==", 120, 120==120)
print("== Igual a:", 120, "==", 150, 120==150)
print("!= Igual a:", 120, "==", 150, 120!=150)
print("!= Igual a:", 120, "!=", 120, 120!=120)
print("> Mayor que:", 250, ">", 200, 250>200)
print("> Mayor que:", 150, ">", 200, 150>200)
print("< Menor que:", 100, "<", 200, 100<200)
print("< Menor que:", 300, "<", 200, 300<200)
print(">= Mayor o igual que:", 200, ">=", 200, 200>=200)
print(">= Mayor o igual que:", 150, ">=", 200, 150>=200)
print("<= Menor o igual que:", 180, "<=", 200, 180<=200)
print("<= Menor o igual que:", 250, "<=", 200, 250<=200)

print("OPERADORES LOGICAS")
print("Operador and: (asientos==asientos) and (precio>100)", (10==10) and (150>100))
print("Operador and: (asientos==asientos) and (precio>500)", (10==10) and (150>500))
print("Operador or: (asientos==asientos) or (precio>500)", (10==10) or (150>500))
print("Operador or: (asientos==asientos) or (precio>500)", (10==12) or (150>500))
print("Operador and: not (precio==500)", not (150==500))
print("Operador and: not (precio==150)", not (150==150))

fondos_suficientes = True
vuelo_disponible = True

reserva_confirmada = fondos_suficientes and vuelo_disponible
print("¿Reserva confirmada?", reserva_confirmada)

es_viajero_frecuente = True
fondos_suficientes = False
embarque_prioritario = es_viajero_frecuente or fondos_suficientes
print("¿Embarque prioritario aprobado?", embarque_prioritario)