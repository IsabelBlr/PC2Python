def es_primo(numero):
    if numero <= 1:
        return False  
    
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False  
    return True  


numero = 17
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")