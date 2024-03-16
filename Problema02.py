numero_filas = 5

for i in range(numero_filas):
    for j in range(i + 1):
        print("*", end=" ")
    print()


for i in range(numero_filas -1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()