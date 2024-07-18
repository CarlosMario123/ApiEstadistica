import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que tienes un DataFrame con tus datos
data = pd.DataFrame({
    'peso_inicial': [1.2, 1.3, 1.1, 1.4, 1.3, 1.2, 1.1, 1.4, 1.3, 1.2],
    'peso_final': [2.5, 2.7, 2.4, 2.8, 2.6, 2.5, 2.4, 2.7, 2.6, 2.5],
    'alimento': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C']
})

# Calcular la ganancia de peso
data['ganancia_peso'] = data['peso_final'] - data['peso_inicial']

# Análisis descriptivo
descriptive_stats = data.groupby('alimento')['ganancia_peso'].describe()
print(descriptive_stats)

# Visualización de datos
sns.boxplot(x='alimento', y='ganancia_peso', data=data)
plt.title('Ganancia de Peso por Tipo de Alimento')
plt.show()

# ANOVA
model = ols('ganancia_peso ~ C(alimento)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# Si ANOVA es significativa, realizar prueba post-hoc de Tukey
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog=data['ganancia_peso'], groups=data['alimento'], alpha=0.05)
print(tukey)
