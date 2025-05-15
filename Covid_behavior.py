import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = "covid_behaviors.csv"
df = pd.read_csv(filename) #AR

#China, South Korea, and India
asian_query = "Country in ['China', 'South Korea', 'India']"
smaller_df = df.query(asian_query)

#Scatter Plot
smaller_df.plot.scatter(x='Country', y='Counts.Handwashes')
plt.title("Handwashing Frequency: China, South Korea, India")
plt.xlabel("Country")
plt.ylabel("Country.Handwashes")
plt.show()
#print(df)
#print(df.describe())
#print(df['Counts.Handwashes','Scores.Masks.Outside home','Scores.Masks.Grocery store','Scores.Masks.Clothing store','Scores.Masks.Work','Scores.Masks.Public transport','Scores.Precautions.Covered mouth sneeze'].describe())
#print (df.groupby('Country')[['Counts.Handwashes','Scores.Masks.Outside home','Scores.Masks.Grocery store','Scores.Masks.Clothing store','Scores.Masks.Work','Scores.Masks.Public transport','Scores.Precautions.Covered mouth sneeze']].agg(['mean', 'std', 'min']))




