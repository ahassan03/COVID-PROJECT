import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = "covid_behaviors.csv"
df = pd.read_csv(filename) #AR

mouth_sneezing = df.groupby('Country')['Scores.Precautions.Covered mouth sneeze'].mean()

mouth_sneezing = mouth_sneezing.sort_values()

plt.figure(figsize=(12, 6))
plt.plot(mouth_sneezing.index, mouth_sneezing.values, marker='o', linestyle='-')
plt.title("Average Covered Mouth When Sneezing by Country")
plt.xlabel("Country")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
