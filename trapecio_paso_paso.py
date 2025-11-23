import numpy as np

# --- CONFIGURACIÓN ---
def f(x):
    return np.sin(x)  # <--- CAMBIA TU FUNCIÓN AQUÍ

a = 0         # Límite inferior
b = np.pi     # Límite superior

print(f"{'Iteración':<10} | {'N (Intervalos)':<15} | {'Resultado Trapecio (Manual)'}")
print("-" * 60)

# Hacemos 10 iteraciones (N = 1, 2, 3... 10)
for n in range(1, 11):
    h = (b - a) / n
    
    # Fórmula: h/2 * [f(a) + f(b) + 2 * Suma_Intermedios]
    
    # Suma de extremos
    suma_extremos = f(a) + f(b)
    
    # Suma de puntos internos
    suma_internos = 0
    for i in range(1, n):
        x_actual = a + i * h
        suma_internos += f(x_actual)
        
    resultado = (h / 2) * (suma_extremos + 2 * suma_internos)
    
    print(f"{n:<10} | {n:<15} | {resultado:.8f}")