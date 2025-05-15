# descriptive_analysis.py

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('covid_behaviors.csv')


print(df.info())        
print(df.describe())   

print(df.head())        

#  compute average counts & scores per country
grouped = df.groupby('Country').agg({
    'Counts.Total contacts': 'mean',
    'Counts.Times left home': 'mean',
    'Counts.Handwashes': 'mean',
    'Scores.Isolate.Willingness if symptoms': 'mean'
}).reset_index()

print(grouped.sort_values('Scores.Isolate.Willingness if symptoms', ascending=False))

# avg handwashes by country
plt.figure(figsize=(8,5))
plt.bar(grouped['Country'], grouped['Counts.Handwashes'])
plt.xticks(rotation=45, ha='right')
plt.title('average daily handwashes by country')
plt.xlabel('country')
plt.ylabel('handwashes per day')
plt.tight_layout()
plt.show()
