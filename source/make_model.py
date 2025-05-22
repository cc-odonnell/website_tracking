# this runs a basic logistic regression
# it prints out an ordered list of coefficients

# library
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# run diagnostics if time allows


def run_logistic_regression(df, target, list_of_features):
    """    Train and evaluate a logistic regression model.    """

    # 1. Subset data
    X = df[list_of_features]
    y = df[target]

    # 2. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Fit model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 4. Predictions and evaluation
    y_pred = model.predict(X_test)
    print("\n Classification Report:\n", classification_report(y_test, y_pred))

    # 5. Feature importance
    feature_importance = pd.Series(model.coef_[0], index=list_of_features)
    print("\n Feature Coefficients:\n", feature_importance.sort_values(ascending=False))

    return model




