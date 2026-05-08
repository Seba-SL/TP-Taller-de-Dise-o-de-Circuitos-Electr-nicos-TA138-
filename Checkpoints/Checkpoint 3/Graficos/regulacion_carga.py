import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Resistencias de carga [ohm]
R = np.array([1000, 470, 100 , 47, 23.5, 8])

# Mediciones de Vo
Vo_mult = np.array([5, 4.99, 4.99, 4.99, 4.98, 3.88])

Vo_osc = np.array([4.82, 4.83, 4.82, 4.81, 4.8, 4.78])

# Interpolacion
R_interp = np.linspace(R.min(), R.max(), 400)

f_mult = interp1d(R, Vo_mult, kind='linear')
f_osc = interp1d(R, Vo_osc, kind='linear')

# Graficar
plt.figure(figsize=(9,5))

# Curvas
plt.plot(R_interp, f_mult(R_interp),label='Vo Multimetro', linewidth = 3)

plt.plot(R_interp, f_osc(R_interp), label='Vo Osciloscopio', linewidth = 3)

# Puntos medidos
plt.scatter(R, Vo_mult)
plt.scatter(R, Vo_osc)

# Etiquetas
plt.xlabel('Resistencia de carga RL [Ω]')
plt.ylabel('Tension de salida Vo [V]')
plt.title('Regulacion de carga del LDO')

plt.grid(True)
plt.legend()


V1_mult = 5 
R1_mult = 1000
V2_mult = 4.99 
R2_mult = 47 

V1_osc = 4.82
V2_osc = 4.82

RT_mult = ((1 - (V1_mult/V2_mult))*R2_mult)/( ((V1_mult/V2_mult)*(R2_mult/R1_mult)) - 1)
RT_osc = ((1 - (V1_mult/V2_mult))*R2_mult)/( ((V1_mult/V2_mult)*(R2_mult/R1_mult)) - 1)




texto = (
    f'Rt_osc = {RT_osc:.2f} Ω\n'
    f'Rt_mult = {RT_mult:.2f} Ω'
)

plt.text(
    750, 4.2,
    texto,
    fontsize=11,
    bbox=dict(facecolor='white', alpha=0.85)
)

# Cartel con valores medidos
texto = (
    'Valores medidos:\n\n'
    f'RL = {R[0]:.1f} Ω  |  Vo_mult = {Vo_mult[0]:.2f} V  |  Vo_osc = {Vo_osc[0]:.2f} V\n'
    f'RL = {R[1]:.1f} Ω  |  Vo_mult = {Vo_mult[1]:.2f} V  |  Vo_osc = {Vo_osc[1]:.2f} V\n'
    f'RL = {R[2]:.1f} Ω  |  Vo_mult = {Vo_mult[2]:.2f} V  |  Vo_osc = {Vo_osc[2]:.2f} V\n'
    f'RL = {R[3]:.1f} Ω  |  Vo_mult = {Vo_mult[3]:.2f} V  |  Vo_osc = {Vo_osc[3]:.2f} V\n'
    f'RL = {R[4]:.1f} Ω  |  Vo_mult = {Vo_mult[4]:.2f} V  |  Vo_osc = {Vo_osc[4]:.2f} V\n'
    f'RL = {R[5]:.1f} Ω  |  Vo_mult = {Vo_mult[5]:.2f} V  |  Vo_osc = {Vo_osc[5]:.2f} V'
)

# Mostrar cartel
plt.text(
    150, 3.95,
    texto,
    fontsize=9,
    bbox=dict(facecolor='white', alpha=0.9)
)


plt.title("Regulación de carga")
plt.show()