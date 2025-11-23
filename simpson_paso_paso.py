import numpy as np

# --- CONFIGURACIÓN ---
def f(x):
    return np.sin(x)  # <--- CAMBIA TU FUNCIÓN AQUÍ

a = 0         # Límite inferior
b = np.pi     # Límite superior

print(f"{'Iteración':<10} | {'N (Intervalos)':<15} | {'Resultado Simpson (Manual)'}")
print("-" * 60)

# Hacemos 10 iteraciones (N debe ser par: 2, 4, 6...)
for k in range(1, 11):
    n = k * 2
    h = (b - a) / n
    
    # Fórmula: h/3 * [f(a) + f(b) + 4*Impares + 2*Pares]
    
    # Suma inicial con los extremos
    suma = f(a) + f(b)
    
    # Iteramos los puntos intermedios
    for i in range(1, n):
        x_actual = a + i * h
        
        if i % 2 == 0:
            suma += 2 * f(x_actual) # Posición Par
        else:
            suma += 4 * f(x_actual) # Posición Impar
            
    resultado = (h / 3) * suma
    
    print(f"{k:<10} | {n:<15} | {resultado:.8f}")