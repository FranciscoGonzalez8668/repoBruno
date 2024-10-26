import numpy as np
from scipy.signal import firwin

# Parámetros del filtro
fs = 22050  # Cambia a 48000 si prefieres esa frecuencia de muestreo
f1 = 1500   # Frecuencia de corte inferior en Hz
f2 = 2300   # Frecuencia de corte superior en Hz
numtaps = 500  # 500 coeficientes (taps) del filtro

# Diseño del filtro FIR pasa banda
coeffs = firwin(numtaps, [f1, f2], pass_zero=False, fs=fs)

# Guardar los coeficientes en un archivo .coeef, separados por comas en una sola línea
with open("filtro_pasa_banda_actualizado.coeef", "w") as f:
    f.write(','.join(map(str, coeffs)))

print(f"Coeficientes del filtro guardados en 'filtro_pasa_banda_actualizado.coeef'.")