# descriptive_analysis.py

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('covid_behaviors.csv')


print(df.info())        
print(df.describe())   

print(df.head())        

grouped = df.groupby('Country').agg({
    'Counts.Total contacts': 'mean',
    'Counts.Times left home': 'mean',
    'Counts.Handwashes': 'mean',
    'Scores.Isolate.Willingness if symptoms': 'mean'
}).reset_index()

print(grouped.sort_values('Scores.Isolate.Willingness if symptoms', ascending=False)) # Witten with the help of AI


plt.figure(figsize=(8,5))
plt.bar(grouped['Country'], grouped['Counts.Handwashes']) # Written with the help of Ai
plt.xticks(rotation=45, ha='right') # Written with the help of Ai
plt.title('Average Daily Handwashes By Country')
plt.xlabel('Country')
plt.ylabel('Handwashes Per Day')
plt.tight_layout()
plt.show()

# CITATION / AI USAGE

# AI Assistance: Line 22
# Reference: Chat‑GPT 4. (2025, May 10). "How do I sort a pandas DataFrame by a column in descending order?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/

# AI Assistance: Line 26
# Reference: Chat‑GPT 4. (2025, May 10). "How can I create a bar chart of aggregated data using matplotlib?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/

# AI Assistance: Line 27
# Reference: Chat‑GPT 4. (2025, May 10). "What's the best way to rotate x‑axis labels in matplotlib for readability?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/
