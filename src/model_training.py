from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

if __name__ == '__main__':
    print("Starting model training...")
    
    # Load the Iris dataset
    print("Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target
    print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")
    
    # Split the data into training and testing sets
    print("\nSplitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
    # Train a Random Forest classifier
    print("\nTraining Random Forest classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    # Save the model to a file
    print("\nSaving model to 'iris_model.pkl'...")
    joblib.dump(model, 'iris_model.pkl')
    
    print("The model training was successful")
    print("Model saved successfully!")