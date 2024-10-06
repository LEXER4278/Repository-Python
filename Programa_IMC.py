#Codigo Hecho por: Lexer Iván Juarez Vargas el 5/10/2024

#Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura, desplegarlos en pantalla junto con su Índice de Masa Corporal (IMC).


while True:
    peso = 0
    altura = 0.0
    edad = 0
    print("¡Hola! Este es un programa para calcular tu indice de masa corporal (IMC)")
    nom = input("Por favor introduzca su nombre: ")
    app = input("Su Apellido Paterno: ")
    apm = input("Su Apellid Materno: ")

    print("Muy bien "+ nom + ", sigamos con los siguientes datos: ")

    while True:
        try:
            edad = int (input ("Edad en años: ")) 
            break
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
    while True:
        try:
            peso = float(input("Ingresa tu peso en kilogramos: "))  # Intenta convertir la entrada a float
            break  # Si tiene éxito, salir del bucle
        except ValueError:  # Captura el error si la conversión falla
            print("Error: Por favor, ingresa un número válido.")

    while True:
        try:
            altura = float(input("Ingresa tu altura en metros: "))  # Intenta convertir la entrada a float
            break  # Si tiene éxito, salir del bucle
        except ValueError:  # Captura el error si la conversión falla
            print("Error: Por favor, ingresa un número válido.")




        

# Operación
    print ("Edad: " + str(edad) + ", Peso: " + str(peso) + " Kg , Altura: " + str(altura) + " M")
    imc = peso / altura ** 2

    print("Imprimiendo datos: \n"+ nom + " "+ app + " "+ apm )
    print("Tu IMC es: " + str(imc))

    if imc < 18.5:
        print("Clasificación: Peso insuficiente (Delgadez)")
    elif imc >= 18.5 and imc <= 24.9:
        print("Clasificación: Peso normal")
    elif imc >= 25.0 and imc <= 29.9:
        print("Clasificación: Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Clasificación: Obesidad Grado 1 (Obesidad leve)")
    elif imc >= 35.0 and imc <= 39.9:
        print("Clasificación: Obesidad Grado 2 (Obesidad moderada)")
    elif imc >= 40.0:
        print("Clasificación: Obesidad Grado 3 (Obesidad mórbida)")






 
    while True:
         respuesta = input("¿Quieres salir? (y/n): ").lower()

         if respuesta == "y":
              print("Saliendo...")
              break
         elif respuesta == "n":
              print("Reiniciando...")
              break
         else:
              print("caracter no valido. por favor ingresar 'y' o 'n'. " )

    if respuesta == "y":
         break
     

        
    
       