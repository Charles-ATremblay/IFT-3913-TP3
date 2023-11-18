import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données depuis le fichier CSV
data = pd.read_csv('jfreechart-test-stats.csv')

# Visualiser la corrélation entre TLOC et TASSERT
print(data.columns)
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.scatter(data['TLOC'], data[' TASSERT'])
plt.title('TLOC vs TASSERT')
plt.xlabel('TLOC')
plt.ylabel('TASSERT')

# Calculer et afficher la droite de régression
coeff_TLOC_TASSERT = np.polyfit(data['TLOC'], data[' TASSERT'], 1)
plt.plot(data['TLOC'], coeff_TLOC_TASSERT[0] * data['TLOC'] + coeff_TLOC_TASSERT[1], color='red')

# Afficher le coefficient de corrélation
corr_TLOC_TASSERT = data['TLOC'].corr(data[' TASSERT'])
print(f"Corrélation entre TLOC et TASSERT : {corr_TLOC_TASSERT}")

# Visualiser la corrélation entre WMC et TASSERT
plt.subplot(1, 3, 2)
plt.scatter(data[' WMC'], data[' TASSERT'])
plt.title('WMC vs TASSERT')
plt.xlabel('WMC')
plt.ylabel('TASSERT')

# Calculer et afficher la droite de régression
coeff_WMC_TASSERT = np.polyfit(data[' WMC'], data[' TASSERT'], 1)
plt.plot(data[' WMC'], coeff_WMC_TASSERT[0] * data[' WMC'] + coeff_WMC_TASSERT[1], color='red')

# Afficher le coefficient de corrélation
corr_WMC_TASSERT = data[' WMC'].corr(data[' TASSERT'])
print(f"Corrélation entre WMC et TASSERT : {corr_WMC_TASSERT}")

# Visualiser la corrélation entre WMC et TLOC
plt.subplot(1, 3, 3)
plt.scatter(data[' WMC'], data['TLOC'])
plt.title('WMC vs TLOC')
plt.xlabel('WMC')
plt.ylabel('TLOC')

# Calculer et afficher la droite de régression
coeff_WMC_TLOC = np.polyfit(data[' WMC'], data['TLOC'], 1)
plt.plot(data[' WMC'], coeff_WMC_TLOC[0] * data[' WMC'] + coeff_WMC_TLOC[1], color='red')

# Afficher le coefficient de corrélation
corr_WMC_TLOC = data[' WMC'].corr(data['TLOC'])
print(f"Corrélation entre WMC et TLOC : {corr_WMC_TLOC}")

plt.show()