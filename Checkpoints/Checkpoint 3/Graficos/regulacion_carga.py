import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# =========================================
# MEDICIONES REALES
# =========================================

# Resistencias de carga [ohm]
R = np.array([1000, 470, 100, 47, 23.5, 8])

# Mediciones de Vo
Vo_mult = np.array([5, 4.99, 4.99, 4.99, 4.98, 3.88])

Vo_osc = np.array([4.82, 4.83, 4.82, 4.81, 4.8, 4.78])

# =========================================
# INTERPOLACION
# =========================================

R_interp = np.linspace(R.min(), R.max(), 400)

f_mult = interp1d(R, Vo_mult, kind='linear')
f_osc = interp1d(R, Vo_osc, kind='linear')

# =========================================
# DATOS LTSPICE
# =========================================

archivo = "/home/sebastian/FIUBA-2do Cuatrimestre/Taller de Diseño Electrónico TA138/TP_Taller_de_Diseño_ TA138_G7/Simulación/LDO/Graficos en Python/Datos de Ltspice/LDO/regulacion_carga_Vo_vsIL.txt"

# Cargar archivo
datos = np.loadtxt(archivo, skiprows=1)

IL = datos[:,0]      # Corriente [A]
Vo_lt = datos[:,1]   # Tension [V]

# =========================================
# CONVERSION A RESISTENCIA
# RL = Vo / IL
# =========================================

# Evitar division por cero
mask = IL > 0

IL = IL[mask]
Vo_lt = Vo_lt[mask]

RL_lt = Vo_lt / IL

# Filtrar valores invalidos
mask_valid = Vo_lt > 0

RL_lt = RL_lt[mask_valid]
Vo_lt = Vo_lt[mask_valid]

# =========================================
# GRAFICO
# =========================================

plt.figure(figsize=(9,5))

# Curvas interpoladas medidas
plt.plot(   R_interp,f_mult(R_interp),label='Vo Multimetro',linewidth=3)

plt.plot( R_interp, f_osc(R_interp), label='Vo Osciloscopio', linewidth=3)

# Puntos medidos
plt.scatter(R, Vo_mult)
plt.scatter(R, Vo_osc)

# Curva LTspice
plt.plot(RL_lt,Vo_lt,'--',linewidth=3,label='Simulación LTspice')

# =========================================
# TEXTOS
# =========================================

plt.xlabel('Resistencia de carga RL [Ω]')
plt.ylabel('Tension de salida Vo [V]')
plt.title('Regulacion de carga del LDO')

plt.grid(True)
plt.legend()

# =========================================
# CALCULO Rt
# =========================================

V1_mult = 5
R1_mult = 1000

V2_mult = 4.99
R2_mult = 47

V1_osc = 4.82
V2_osc = 4.82

RT_mult = (
    ((1 - (V1_mult/V2_mult))*R2_mult) /
    (((V1_mult/V2_mult)*(R2_mult/R1_mult)) - 1)
)

RT_osc = (
    ((1 - (V1_mult/V2_mult))*R2_mult) /
    (((V1_mult/V2_mult)*(R2_mult/R1_mult)) - 1)
)

texto = (
    f'Rt_osc = {RT_osc:.2f} Ω\n'
    f'Rt_mult = {RT_mult:.2f} Ω'
)

plt.text(
    750,
    4.2,
    texto,
    fontsize=11,
    bbox=dict(facecolor='white', alpha=0.85)
)

# =========================================
# CARTEL MEDICIONES
# =========================================

texto = (
    'Valores medidos:\n\n'
    f'RL = {R[0]:.1f} Ω  |  Vo_mult = {Vo_mult[0]:.2f} V  |  Vo_osc = {Vo_osc[0]:.2f} V\n'
    f'RL = {R[1]:.1f} Ω  |  Vo_mult = {Vo_mult[1]:.2f} V  |  Vo_osc = {Vo_osc[1]:.2f} V\n'
    f'RL = {R[2]:.1f} Ω  |  Vo_mult = {Vo_mult[2]:.2f} V  |  Vo_osc = {Vo_osc[2]:.2f} V\n'
    f'RL = {R[3]:.1f} Ω  |  Vo_mult = {Vo_mult[3]:.2f} V  |  Vo_osc = {Vo_osc[3]:.2f} V\n'
    f'RL = {R[4]:.1f} Ω  |  Vo_mult = {Vo_mult[4]:.2f} V  |  Vo_osc = {Vo_osc[4]:.2f} V\n'
    f'RL = {R[5]:.1f} Ω  |  Vo_mult = {Vo_mult[5]:.2f} V  |  Vo_osc = {Vo_osc[5]:.2f} V'
)

plt.text(
    150,
    3.95,
    texto,
    fontsize=9,
    bbox=dict(facecolor='white', alpha=0.9)
)

# =========================================
# MOSTRAR
# =========================================

plt.show()