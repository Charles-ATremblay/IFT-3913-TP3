import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données depuis le fichier CSV
data = pd.read_csv('jfreechart-test-stats.csv')

# Visualiser la corrélation entre TLOC et TASSERT
print(data.columns)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
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

plt.show()