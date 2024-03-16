def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"  
    nueva_cadena = ""  
    for char in cadena:
        if char not in vocales:  
            nueva_cadena += char
    return nueva_cadena


texto_original = input("Ingrese una cadena de texto: ")


texto_sin_vocales = omitir_vocales(texto_original)
print("Texto sin vocales:", texto_sin_vocales)
