import pandas as pd
from scipy import stats

# Charger les données depuis le fichier CSV
data = pd.read_csv('jfreechart-test-stats.csv')

# Créer deux groupes en fonction du nombre d'assertions
groupe_plus_20_assertions = data[data[' TASSERT'] > 20]
groupe_moins_20_assertions = data[data[' TASSERT'] <= 20]

# Effectuer le test t de Student pour TLOC
t_stat_TLOC, p_value_TLOC = stats.ttest_ind(groupe_plus_20_assertions['TLOC'], groupe_moins_20_assertions['TLOC'])

# Effectuer le test t de Student pour WMC
t_stat_WMC, p_value_WMC = stats.ttest_ind(groupe_plus_20_assertions[' WMC'], groupe_moins_20_assertions[' WMC'])

# Afficher les résultats
print(f"Test t de Student pour TLOC : Statistique={t_stat_TLOC}, P-valeur={p_value_TLOC}")
print(f"Test t de Student pour WMC : Statistique={t_stat_WMC}, P-valeur={p_value_WMC}")

# Interpréter les résultats
alpha = 0.05
if p_value_TLOC < alpha:
    print("Il y a une différence significative dans TLOC entre les deux groupes. ==> complexité plus élevée pour les classes ayant plus de 20 assertions")
else:
    print("Il n'y a pas de différence significative dans TLOC entre les deux groupes.")

if p_value_WMC < alpha:
    print("Il y a une différence significative dans WMC entre les deux groupes. ==> complexité plus élevée pour les classes ayant plus de 20 assertions")
else:
    print("Il n'y a pas de différence significative dans WMC entre les deux groupes.")