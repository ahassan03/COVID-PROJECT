import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "./covid_behaviors.csv"
df = pd.read_csv(filename)

#BOXPLOT
df = df.query("Country == 'Germany' or Country == 'Spain' or Country == 'Italy'")
df.boxplot(column="Scores.Masks.Outside home",by='Country', grid=False) # Written with the help of AI.
plt.title("Mask-Wearing Scores outside home by country")
plt.xlabel('Country')
plt.ylabel('Score')
plt.ylim(0,100) # Written with the help of AI.
plt.show()

# BAR CHART
columns = df.columns.str.strip()
countries_of_interest = ['Germany', 'Spain', 'Italy']
filtered_df = df[df['Country'].isin(countries_of_interest)] # Written with the help of AI.
plt.bar(filtered_df['Country'], filtered_df['Scores.Masks.Outside home'], color='skyblue') # Written with the help of AI.
plt.xlabel('Country')
plt.ylabel('Mask-Wearing Score (outside home)')
plt.title('Masks-Wearing Scores in Selected Countries')
plt.ylim(0,100) # Written with the help of AI.
plt.show()

#CORRELATION MATRIX for all
corr_matrix = df.corr(numeric_only=True).round(2) # Written with the help of AI.
sns.heatmap(corr_matrix, annot=True, vmax=1,cmap='icefire') # Written with the help of AI.
plt.show()
 
 # Chat-GPT4.(2025/May/16). "Help me create a boxplot for three countries under a single "Country" column." Generated using OpenAi Chat-GPT. https://chat.openai.com/ 
 # Chat-GPT4.(2025/May/16). "Help me create a bar chart for three countries under a single "Country" column." Generated using OpenAi Chat-GPT. https://chat.openai.com/ 
 # Chat-GPT4.(2025/May/16). "Help me create a correlation matrix showing a heatmap with the visuals of 'icefire'." Generated using OpenAi Chat-GPT. https://chat.openai.com/ 
