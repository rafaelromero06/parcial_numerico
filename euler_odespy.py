import numpy as np
import math

# ==========================================
# 1. BLOQUE DE CONFIGURACIÓN (MODIFICA AQUÍ)
# ==========================================

# Define la función f(t, y) de la ecuación y' = f(t, y)
def f_user(t, y):
    # Ejemplo: y' = y - t^2 + 1
    return y - t**2 + 1

# Define la Solución Exacta (necesaria para calcular el error e_N de la imagen 1)
def solucion_exacta(t):
    # Solución analítica del ejemplo: y(t) = (t+1)^2 - 0.5 * e^t
    return (t + 1)**2 - 0.5 * np.exp(t)

# Condiciones Iniciales
t0 = 0.0          # Tiempo inicial
y0 = 0.5          # Valor inicial y(0)
tf = 2.0          # Tiempo final (donde evaluamos el error)
num_iteraciones = 10 # Cuántas veces vamos a refinar la malla

# ==========================================
# 2. IMPLEMENTACIÓN MANUAL
# ==========================================

def euler_manual():
    print(f"{'N (Pasos)':<10} | {'h (Tamaño)':<12} | {'Aprox y(tf)':<15} | {'Error Global':<15} | {'Orden (p)':<10}")
    print("-" * 85)

    errores = [] # Guardamos errores para calcular 'p' (formula imagen 1)
    ns = []      # Guardamos los N

    for k in range(1, num_iteraciones + 1):
        # Aumentamos los pasos progresivamente (ej: 10, 20, 40, 80...)
        # Usamos potencias de 2 para ver mejor la reducción del error a la mitad
        N = 10 * (2 ** (k-1)) 
        h = (tf - t0) / N
        
        # Algoritmo de Euler (Imagen 2)
        t = t0
        y = y0
        
        for _ in range(N):
            pendiente = f_user(t, y)
            y = y + h * pendiente  # y_{j+1} = y_j + h * f(t, y)
            t = t + h
            
        # Calculamos Error (Imagen 1: |y(tn) - yn|)
        val_exacto = solucion_exacta(tf)
        error = abs(val_exacto - y)
        
        # Calculamos el orden de convergencia p (Fórmula logarítmica de Imagen 1)
        p_str = "-"
        if len(errores) > 0:
            e_prev = errores[-1]
            N_prev = ns[-1]
            # p ≈ log(error_2 / error_1) / log(N_1 / N_2)
            # Como duplicamos N, log(N1/N2) es log(0.5).
            p = np.log(error / e_prev) / np.log(N_prev / N)
            p_str = f"{p:.4f}"

        errores.append(error)
        ns.append(N)
        
        print(f"{N:<10} | {h:<12.5f} | {y:.8f}        | {error:.8f}        | {p_str}")

if __name__ == "__main__":
    print("--- MÉTODO DE EULER (MANUAL) ---")
    euler_manual()