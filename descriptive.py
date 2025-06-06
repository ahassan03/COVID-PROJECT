import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = "covid_behaviors.csv"
df = pd.read_csv(filename) #AR

#mask_outside = df.groupby('Country')['Scores.Masks.Outside home'].mean()   #Assistance  Slides

#mask_outside = mask_outside.sort_values()

#Plot line graph
#plt.figure(figsize=(12,6))
#plt.plot(mask_outside.index, mask_outside.values, marker='o', linestyle='-', color='green')  #Assistance AI
#plt.title("Average Mask Usage Outside Home by Country")
#plt.xlabel("Country")
#plt.ylabel("Scores.Masks.Outside home")
#plt.xticks(rotation=45)
#plt.grid(True)
#plt.tight_layout()
#plt.show()

mouth_sneezing = df.groupby('Country')['Scores.Precautions.Covered mouth sneeze'].mean() #Assistance  Slides

mouth_sneezing = mouth_sneezing.sort_values()

plt.figure(figsize=(12, 6))
plt.plot(mouth_sneezing.index, mouth_sneezing.values, marker='o', linestyle='-')    #Assistance AI
plt.title("Average Covered Mouth When Sneezing by Country")
plt.xlabel("Country")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


#CITATION Power Point Slides

# Fairbanks, Dallin. (April 2025). Descriptive Analytics [Slides 7,8,9,14,15,24].
# CIS 3330 – Analytic Programming Tools, UTEP. 

# AI Assistance: Line 14 & 28
# Reference: Chat‑GPT 4. (2025, May)."How do I plot the average of a column after grouping by country in Python?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/