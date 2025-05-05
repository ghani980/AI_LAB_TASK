import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("Iris.csv")

iris = load_iris()
X = iris.data       # Features
y = iris.target     # Labels

# Step 1: Train-Test Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Choose the right algorithm (Random Forest Classifier is good for classification tasks)
model = RandomForestClassifier(random_state=42)

# Step 3: Apply Classifier
model.fit(X_train, y_train)

# Step 4: Testing / Predicting
y_pred = model.predict(X_test)

# Step 5: Display Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
