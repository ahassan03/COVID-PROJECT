# ols_regression.py

import pandas as pd
import numpy as np
import statsmodels.api as sm

# 1. load your data (make sure covid_behaviors.csv sits alongside this script)
csv_path = "covid_behaviors.csv"
df = pd.read_csv(csv_path)

# 2. inspect column names so you know the exact target header
print("available columns:")
for col in df.columns:
    print("  ", col)

# 3. set your dependent variable
#    look for the column that matches covered-mouth‐sneezing— 
#    it might be something like "Scores.Precautions.Covered mouth sneeze"
target_col = "Scores.Precautions.Covered mouth sneeze"
y = df[target_col]

# 4. build your predictors from all other numeric columns
X = df.select_dtypes(include=[np.number]).drop(columns=[target_col])

# 5. add a constant term (intercept) to the model
X = sm.add_constant(X)

# 6. fit the OLS regression
model = sm.OLS(y, X).fit()

# 7. show the full summary
print(model.summary())
