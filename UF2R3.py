def obtener_numero_valido(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("introduce un numero valido")

def principal():
    print("¡Bienvenido al juego de matemáticas!")
    
    numero1 = obtener_numero_valido("Introduce el primer numero: ")
    numero2 = obtener_numero_valido("Introduce el segundo numero: ")
    
    suma_correcta = numero1 + numero2
    
    print(f"\n¿Cuánto es {numero1} + {numero2}?")
    
    # Bucle principal del juego
    while True:
        try:
            respuesta = float(input("Tu respuesta: "))
            
            if respuesta == suma_correcta:
                print("Correcto")
                break
            elif respuesta > suma_correcta:
                print("Te has pasado")
            else:
                print("Te has quedado corto")
                
        except ValueError:
            print("introduce un numero valido")
principal()