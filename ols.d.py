# ols_regression.py

import pandas as pd
import numpy as np
import statsmodels.api as sm

csv_path = "covid_behaviors.csv"
df = pd.read_csv(csv_path)

print("available columns:")
for col in df.columns: # Written with the help of AI
    print("  ", col) # Written with the help of AI


target_col = "Scores.Precautions.Covered mouth sneeze"
y = df[target_col]

X = df.select_dtypes(include=[np.number]).drop(columns=[target_col]) # Written with the help of AI


X = sm.add_constant(X)

model = sm.OLS(y, X).fit()


print(model.summary())

# CITATION / AI USAGE

# AI Assistance: Line 11
# Reference: Chat‑GPT 4. (2025, May 15). "Can you show me how to loop over a pandas DataFrame’s columns and print each one?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/

# AI Assistance: Line 12
# Reference: Chat‑GPT 4. (2025, May 15). "What's the simplest way to print each column name with indentation inside a Python for‑loop?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/

# AI Assistance: Line 18
# Reference: Chat‑GPT 4. (2025, May 15). "How can I select only numeric columns from a pandas DataFrame and drop a specified column using select_dtypes?" Generated using OpenAI Chat‑GPT. https://chat.openai.com/
