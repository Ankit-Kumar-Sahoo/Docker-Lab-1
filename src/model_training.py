from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

if __name__ == '__main__':
    print("Starting model training...")
    
    # Load the Wine dataset
    print("Loading Wine dataset...")
    wine = load_wine()
    X, y = wine.data, wine.target
    print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")
    
    # Split the data into training and testing sets
    print("\nSplitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
    # Train an AdaBoost classifier
    print("\nTraining AdaBoost classifier...")
    base_estimator = DecisionTreeClassifier(max_depth=1)
    model = AdaBoostClassifier(
        estimator=base_estimator,
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluate the model
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    # Save the model to a file
    print("\nSaving model to 'wine_model.pkl'...")
    joblib.dump(model, 'wine_model.pkl')
    
    print("The model training was successful")
    print("Model saved successfully!")