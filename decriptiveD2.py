# time_series_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# 1. load data
df = pd.read_csv('covid_behaviors.csv')

# 2. compute overall mean handwashes per day
overall = (
    df
    .groupby('Days since outbreak')['Counts.Handwashes']
    .mean()
    .reset_index(name='Mean.Handwashes')
)

# 3. plot overall trend
plt.figure(figsize=(8,5))
plt.plot(overall['Days since outbreak'], overall['Mean.Handwashes'], marker='o')
plt.title('average handwashes over time (all countries)')
plt.xlabel('days since outbreak')
plt.ylabel('handwashes per day')
plt.tight_layout()
plt.show()


# 4. compute per‐country time series
ts_country = (
    df
    .pivot_table(
        index='Days since outbreak',
        columns='Country',
        values='Counts.Handwashes',
        aggfunc='mean'
    )
    .sort_index()
)

# 5. plot each country on the same axes
plt.figure(figsize=(10,6))
for country in ts_country.columns:
    plt.plot(ts_country.index, ts_country[country], label=country)
plt.title('average handwashes over time by country')
plt.xlabel('days since outbreak')
plt.ylabel('handwashes per day')
plt.legend(title='country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()