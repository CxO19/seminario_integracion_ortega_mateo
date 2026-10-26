#Condicional If

print("Condicional If")
print("Condicional Simple")

dinero = 10
if dinero >= 5:
    print("Homero puede comprar rosquillas")

print("Programa Finalizo")


print ("Condicional If - else")
print ("Condicional Dos Caminos")

creditos = float (input("Cantidad de creditos disponibles"))
precio_repuesto = (float("Precio repuesto"))

if (creditos >= precio_repuesto):
    print ("Compra Autorizada")
else:
    print ("Creditos Insuficientes")
    print ("Buscar solucion o trueque")


print ("Condicional If -elif - else")
print ("Condicional Condiciones Multiples")

combustible = float (input("Combustible de la nave"))

if (combustible >= 75):
    print ("Optimo")
elif (combustible >= 50):
    print ("Suficiente")
elif (combustible >= 20):
    print ("Bajo")
else:
    print ("Critico")
    print ("Localiza Base mas cercana")


piloto = input ("Nombre del Piloto")
motor_funciona = input ("El motor funcviona (SI/NO)")
combustible = input ("Combustible disponible")

if (motor_funciona == "SI"):
    print ("Motor Verificado")
    if combustible >= 50:
        print ("Combustible suficiente")
        print ("participacion Autorizada")
    else: 
        print("debe recargar combustible")
else:
    print("No puede participar")
    print("El motor necesita reparacion")