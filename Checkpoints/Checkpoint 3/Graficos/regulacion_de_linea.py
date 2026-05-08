import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# =========================================
# Tension de alimentacion Vcc [V]
# =========================================

Vcc = np.array([5.05, 5.26, 6.13, 8.11, 10.39, 15.21, 16.46])

# =========================================
# Mediciones de Vo
# =========================================

# Multimetro
Vo_mult = np.array([4.85, 4.99, 4.99, 4.99, 5.00, 5.00, 5.0])

# Osciloscopio
Vo_osc = np.array([4.65, 4.83, 4.84, 4.84, 4.85, 4.85, 4.85])

# =========================================
# Interpolacion
# =========================================

Vcc_interp = np.linspace(Vcc.min(), Vcc.max(), 400)

f_mult = interp1d(Vcc, Vo_mult, kind='linear')
f_osc = interp1d(Vcc, Vo_osc, kind='linear')

# =========================================
# Figura
# =========================================

plt.figure(figsize=(10,5))

# Curvas interpoladas
plt.plot(Vcc_interp, f_mult(Vcc_interp),linewidth=3, label='Vo Multimetro')
plt.plot(Vcc_interp, f_osc(Vcc_interp),linewidth=3,label='Vo Osciloscopio')

# Puntos medidos
plt.scatter(Vcc, Vo_mult)
plt.scatter(Vcc, Vo_osc)

# =========================================
# Etiquetas
# =========================================

plt.xlabel('Tension de alimentacion Vcc [V]')
plt.ylabel('Tension de salida Vo [V]')
plt.title('Regulacion de linea del LDO')

plt.grid(True)
plt.legend()

# =========================================
# Calculo regulacion de linea
# =========================================

Vo1_mult = Vo_mult[1]
Vo2_mult = Vo_mult[-1]

Vo1_osc = Vo_osc[1]
Vo2_osc = Vo_osc[-1]

Vcc1 = Vcc[1]
Vcc2 = Vcc[-1]

Reg_mult = (Vo2_mult - Vo1_mult) / (Vcc2 - Vcc1)

Reg_osc = (Vo2_osc - Vo1_osc) / (Vcc2 - Vcc1)

# =========================================
# Cartel
# =========================================

texto = (
    'Regulacion de linea\n\n'

    f'Vcc1 = {Vcc1:.2f} V\n'
    f'Vcc2 = {Vcc2:.2f} V\n'

    f'Multimetro:\n'
    f'Vo1 = {Vo1_mult:.2f} V\n'
    f'Vo2 = {Vo2_mult:.2f} V\n'
    f'RL_mult = {Reg_mult:.5f} V/V\n\n'

    f'Osciloscopio:\n'
    f'Vo1 = {Vo1_osc:.2f} V\n'
    f'Vo2 = {Vo2_osc:.2f} V\n'
    f'RL_osc = {Reg_osc:.5f} V/V'
)

plt.text(
    15, 4.64,
    texto,
    fontsize=9,
    bbox=dict(facecolor='white', alpha=0.9)
)

# Limites eje Y
plt.ylim(4.6, 5.1)

plt.show()