import joblib
from preprocess import preprocess_data

# Load dataset
data = preprocess_data("datasets/network_data.csv")

# Train a simple model
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
X, y = data.drop("target", axis=1), data["target"]
model.fit(X, y)

# Save model
joblib.dump(model, "models/load_balancer.pkl")
print("ML Model Trained!")
