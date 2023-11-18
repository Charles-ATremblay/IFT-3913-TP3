import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv('jfreechart-test-stats.csv')

# Nettoyer les noms de colonnes en enlevant les espaces éventuels
cleaned_columns = [col.strip() for col in data.columns]

# Remplacer les noms de colonnes dans le DataFrame
data.columns = cleaned_columns

# Visualiser les boîtes à moustaches pour TLOC, WMC, TASSERT
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Boxplot for TLOC
data['TLOC'].plot(kind='box', ax=axes[0])
axes[0].set_title('Boxplot for TLOC')

# Boxplot for WMC
data['WMC'].plot(kind='box', ax=axes[1])
axes[1].set_title('Boxplot for WMC')

# Boxplot for TASSERT
data['TASSERT'].plot(kind='box', ax=axes[2])
axes[2].set_title('Boxplot for TASSERT')

plt.show()

# Calculate relevant statistics
statistics = data.describe()

# Print the statistics
# count - The number of not-empty values.
# mean - The average (mean) value.
# std - The standard deviation.
# min - the minimum value.
# 25% - The 25% percentile*.
# 50% - The 50% percentile*.
# 75% - The 75% percentile*.
# max - the maximum value.

# *Percentile meaning: how many of the values are less than the given percentile. Read more about percentiles in our Machine Learning Percentile chapter.
#(Found on https://www.w3schools.com/python/pandas/ref_df_describe.asp#:~:text=The%20describe()%20method%20returns,The%20average%20(mean)%20value.)
print(statistics)