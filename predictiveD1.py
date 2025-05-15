# predictive_analysis.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# 1. load data
df = pd.read_csv('covid_behaviors.csv')

# define a binary target:
#  whether someone is highly willing to isolate if they have symptoms
#  threshold at 80 (you can adjust)
df['will_isolate'] = (df['Scores.Isolate.Willingness if symptoms'] >= 80).astype(int)

# 3. select numeric predictors
features = [
    'Counts.Household contacts',
    'Counts.Total contacts',
    'Counts.Times left home',
    'Counts.Handwashes',
    'Scores.Outlooks.Covid is dangerous',
    'Scores.Outlooks.Likely to get covid'
]
X = df[features].fillna(0)
y = df['will_isolate']

# 4. split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 5. scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# 6. train logistic regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 7. evaluate
y_pred = model.predict(X_test_scaled)
print("accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
