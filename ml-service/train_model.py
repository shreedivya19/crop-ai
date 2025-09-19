import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

data = {
    'N': [40, 50, 30, 60, 70, 20],
    'P': [20, 30, 10, 35, 80, 15],
    'K': [40, 50, 60, 55, 43, 65],
    'pH': [6.5, 7.0, 6.0, 6.8, 7.2, 6.3],
    'temperature': [25, 30, 22, 28, 32, 20],
    'humidity': [80, 65, 70, 75, 60, 85],
    'rainfall': [100, 200, 90, 150, 180, 75],
    'crop': ['rice', 'wheat', 'rice', 'cotton', 'wheat', 'cotton']
}

df = pd.DataFrame(data)

X = df[['N', 'P', 'K', 'pH', 'temperature', 'humidity', 'rainfall']]
y = df['crop']

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'crop_model.pkl')
joblib.dump(le, 'label_encoder.pkl')

score = model.score(X_test, y_test)
print(f"Model accuracy: {score:.2f}")
