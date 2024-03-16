def contar_digitos(numero, digito):
    
    numero_str = str(numero)
    
    cantidad = numero_str.count(str(digito))
    return cantidad

numero_ingresado = 15789000
digito = 0
cantidad = contar_digitos(numero_ingresado, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad}")