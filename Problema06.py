def fibonacci(limite):
    
    a, b = 0, 1
    fibonacci_series = [a, b]  
 
    while b < limite:
        a, b = b, a + b  
        if b < limite:  
            fibonacci_series.append(b)
    return fibonacci_series

serie_fibonacci = fibonacci(50)

print("Serie de Fibonacci hasta 50:")
print(serie_fibonacci)