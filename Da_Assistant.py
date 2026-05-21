import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Create dataset (synthetic)


# Target variable (exam score)
data['score'] = (
    5 * data['study_hours'] +
    2 * data['sleep_hours'] +
    0.3 * data['attendance'] +
    np.random.normal(0, 5, 100)
)

# Step 2: Split data
X = data[['study_hours', 'sleep_hours', 'attendance']]
y = data['score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 3: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict
y_pred = model.predict(X_test)

# Step 5: Evaluate
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 6: Visualization
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores")
plt.show()