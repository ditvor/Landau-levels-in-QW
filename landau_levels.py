import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.set_size_inches(12, 7.93)
ax = fig.add_subplot(1, 1, 1)

h_bar = 6.585 * 10 ** (-16)  # reduced planck constant
m_0 = 9.1 * 10 ** (-31)  # electron mass in kg
e = 1.6 * 10 ** (-19)  # electron charge in Coulombs, 1 C = 1 A * 1 s
H = 1  # magnetic field in Tesla, 1 T = kg * c^(-2) * A^(-1)
m_eff_e1 = 0.0255 * m_0
m_eff_h1 = 0.4 * m_0

magnetic_field = np.arange(0, 1.01, 0.01)

# for electrons in QW:

energy_e1 = h_bar * e * magnetic_field / m_eff_e1  # energy value in eV

for i in range(10):
    # Some additional energy (0.008) was added so Landau levels start not from 0 energy point.
    # This allow the landau levels to cross magnetic field in right position
    landau_level_e1 = (energy_e1 * (
                i + 0.5)) * 1000  # multiplied by 1000 in order to get the energy in meV (instead of eV)

    plt.plot(magnetic_field, landau_level_e1, 'red')

# Fermi level

plt.axhline(y=11, color='b', linestyle='--')
plt.axhline(y=16, color='black', linestyle='--')
plt.axhline(y=1.5, color='green', linestyle='--')

# PIRO peaks positions
plt.axvline(x=0.66, color='black', linestyle='--')
plt.axvline(x=0.22, color='black', linestyle='--')
# for holes in QW:

energy_h1 = h_bar * e * magnetic_field / m_eff_h1  # energy value in eV

for i in range(10):
    landau_level_h1 = (0.0045 - energy_h1 * (
                i + 0.5)) * 1000  # multiplied by 1000 in order to get the energy in meV (instead of eV)

    plt.plot(magnetic_field, landau_level_h1, 'blue')

plt.ylim(0, 20)
plt.xlim(0, 1)
ax.set_xticks(np.arange(0, 1.01, 0.1))

plt.grid(alpha=.4, linestyle='--')
plt.title('Landau levels', size=20)
plt.ylabel('Energy, meV', size=14)
plt.xlabel('Magnetic field, T', size=14)
plt.legend()
plt.show()
fig.savefig("Landau_levels.jpg")
