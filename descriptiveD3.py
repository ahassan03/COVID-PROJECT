# rf_classification_english.py

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report

# 1. load & filter
df = pd.read_csv('covid_behaviors.csv')
english_countries = ['Australia', 'Canada', 'United Kingdom', 'United States']
df = df[df['Country'].isin(english_countries)]

# 2. create binary target
df['will_isolate'] = (df['Scores.Isolate.Willingness if symptoms'] >= 80).astype(int)

# 3. select features & target
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

# 4. train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 5. fit random forest
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

# 6. evaluate
y_pred  = rf.predict(X_test)
y_proba = rf.predict_proba(X_test)[:,1]
print("Accuracy:", rf.score(X_test, y_test))
print("ROC AUC:", roc_auc_score(y_test, y_proba))
print(classification_report(y_test, y_pred))

# 7. cross‐validation AUC
cv_scores = cross_val_score(rf, X, y, cv=5, scoring='roc_auc')
print("5-fold CV AUC:", cv_scores.mean())
