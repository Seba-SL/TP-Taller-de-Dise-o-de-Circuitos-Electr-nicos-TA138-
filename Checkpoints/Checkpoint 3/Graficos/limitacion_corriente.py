import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# =========================================
# Corriente de carga Io [A]
# =========================================

Io = np.array([0.00, 0.05, 0.10, 0.20, 0.35, 0.50])

# =========================================
# Tension de salida Vo [V]
# =========================================

Vo_mult = np.array([5.00, 4.99, 4.98, 4.90, 3.20, 1.10])


# =========================================
# Interpolacion
# =========================================

Io_interp = np.linspace(Io.min(), Io.max(), 400)

f_mult = interp1d(Io, Vo_mult, kind='linear')

# =========================================
# Figura
# =========================================

plt.figure(figsize=(10,5))

# Curvas interpoladas
plt.plot(Io_interp,
         f_mult(Io_interp),
         linewidth=3,
         label='Vo Multimetro')



# Puntos medidos
plt.scatter(Io, Vo_mult)

# =========================================
# Etiquetas
# =========================================

plt.xlabel('Corriente de carga Io [A]')
plt.ylabel('Tension de salida Vo [V]')
plt.title('Limitacion de corriente Foldback')

plt.grid(True)
plt.legend()

# =========================================
# Parametros Foldback
# =========================================

# Corriente limite aproximada
I_lim_mult = Io[3]
I_lim_osc = Io[3]

# Tension minima
Vo_min_mult = np.min(Vo_mult)
Vo_min_osc = np.min(Vo_osc)

# =========================================
# Cartel
# =========================================

texto = (
    'Parametros Foldback\n\n'

    f'Multimetro:\n'
    f'I_lim = {I_lim_mult:.2f} A\n'
    f'Vo_min = {Vo_min_mult:.2f} V\n\n'

    f'Osciloscopio:\n'
    f'I_lim = {I_lim_osc:.2f} A\n'
    f'Vo_min = {Vo_min_osc:.2f} V'
)

plt.text(
    0.28, 1.8,
    texto,
    fontsize=9,
    bbox=dict(facecolor='white', alpha=0.9)
)

plt.ylim(0, 5.3)

plt.show()