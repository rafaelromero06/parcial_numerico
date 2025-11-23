import numpy as np
from scipy.integrate import trapezoid

# --- CONFIGURACIÓN ---
def f(x):
    return np.sin(x)  # <--- CAMBIA TU FUNCIÓN AQUÍ

a = 0         # Límite inferior
b = np.pi     # Límite superior

print(f"{'Iteración':<10} | {'N (Intervalos)':<15} | {'Resultado Trapecio (Lib)'}")
print("-" * 60)

# Hacemos 10 iteraciones. Trapecio acepta cualquier N (1, 2, 3...)
for n in range(1, 11):
    
    # 1. Crear los puntos (x) y evaluar la función (y)
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # 2. Calcular usando la librería
    resultado = trapezoid(y, x=x)
    
    print(f"{n:<10} | {n:<15} | {resultado:.8f}")