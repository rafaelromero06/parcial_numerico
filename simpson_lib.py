import numpy as np
from scipy.integrate import simpson

# --- CONFIGURACIÓN ---
def f(x):
    return np.sin(x)  # <--- CAMBIA TU FUNCIÓN AQUÍ

a = 0         # Límite inferior
b = np.pi     # Límite superior

print(f"{'Iteración':<10} | {'N (Intervalos)':<15} | {'Resultado Simpson (Lib)'}")
print("-" * 60)

# Hacemos 10 iteraciones
# Simpson necesita N par, así que iremos de 2 en 2 (2, 4, 6... 20)
for k in range(1, 11):
    n = k * 2
    
    # 1. Crear los puntos (x) y evaluar la función (y)
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # 2. Calcular usando la librería
    resultado = simpson(y, x=x)
    
    print(f"{k:<10} | {n:<15} | {resultado:.8f}")