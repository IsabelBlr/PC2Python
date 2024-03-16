numeros = []  
num_pares = 0  
num_impares = 0  

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)  
        
        if numero % 2 == 0:
            num_pares += 1  # Incrementar el contador de números pares
        else:
            num_impares += 1  # Incrementar el contador de números impares
    elif respuesta == "NO":
        break  
    else:
        print("Respuesta no válida. Por favor, responda SI o NO.")

print("Números ingresados:", numeros)
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)