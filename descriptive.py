import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = "covid_behaviors.csv"
df = pd.read_csv(filename) #AR

mask_outside = df.groupby('Country')['Scores.Masks.Outside home'].mean()

mask_outside = mask_outside.sort_values()

#Plot line graph
plt.figure(figsize=(12,6))
plt.plot(mask_outside.index, mask_outside.values, marker='o', linestyle='-', color='green')
plt.title("Average Mask Usage Outside Home by Country")
plt.xlabel("Country")
plt.ylabel("Scores.Masks.Outside home")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()