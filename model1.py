import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select relevant features for the analysis.
    
    Args:
        df (pd.DataFrame): The input DataFrame with student data.
        
    Returns:
        pd.DataFrame: The feature matrix X.
    """
    # TODO: Select only the required columns from the DataFrame.
    # Recommended: ['Age at enrollment', 'Gender', 'Debtor', 
    #               'Tuition fees up to date', 'Curricular units 1st sem (approved)']
    
    features = ['Age at enrollment', 'Gender', 'Debtor', 'Tuition fees up to date', 'Curricular units 1st sem (approved)']
    X = df[features]
    return X


def handle_missing_values(X: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in the dataset.

    Args:
        X (pd.DataFrame): The input feature matrix.
    
    Returns:
        pd.DataFrame: The feature matrix with missing values handled.
    """
    X = X.copy()

    # TODO: Fill missing values in categorical columns (e.g., Gender, Debtor, etc.) with 'Unknown'.
    categorical_cols = ['Gender', 'Debtor', 'Tuition fees up to date']
    X.loc[:, categorical_cols] = X[categorical_cols].fillna('Unknown')

    # TODO: Fill missing values in numerical columns (e.g., Age, Approved units) with their median.
    numerical_cols = ['Age at enrollment', 'Curricular units 1st sem (approved)']
    X.loc[:, numerical_cols] = X[numerical_cols].fillna(X[numerical_cols].median())

    return X


def encode_categorical_features(X: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical features into numeric format using one-hot encoding.
    
    Args:
        X (pd.DataFrame): The input feature matrix.
        
    Returns:
        pd.DataFrame: The feature matrix with one-hot encoding applied.
    """
    # TODO: Use pd.get_dummies to convert categorical variables into binary columns.
    # Use drop_first=True to avoid dummy variable trap.
    categorical_cols = ['Gender', 'Debtor', 'Tuition fees up to date']
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    return X


def split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.3) -> tuple:
    """
    Split the dataset into training and testing sets.
    
    Args:
        X (pd.DataFrame): The feature matrix.
        y (pd.Series): The target variable.
        test_size (float): Proportion of data to use for testing.
        
    Returns:
        tuple: The train-test split of X and y.
    """
    # TODO: Use train_test_split from sklearn to split data into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test


def train_decision_tree(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    """
    Train a DecisionTreeClassifier on the training data.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training labels.
        
    Returns:
        DecisionTreeClassifier: The trained decision tree model.
    """
    # TODO: Initialize and train a DecisionTreeClassifier using sklearn.
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: DecisionTreeClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> tuple:
    """
    Evaluate the model using accuracy and confusion matrix.
    
    Args:
        model (DecisionTreeClassifier): The trained model.
        X_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing labels.
        
    Returns:
        tuple: Model accuracy and confusion matrix.
    """
    # TODO: Use model.predict() to get predictions.
    # TODO: Use model.score() to get accuracy.
    # TODO: Use confusion_matrix from sklearn.metrics to evaluate the predictions.
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, cm


def apply_l2_regularization(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series) -> LogisticRegression:
    """
    Apply L2 regularization (Ridge) using Logistic Regression.
    
    Returns:
        LogisticRegression: The trained L2 regularized model.
    """
    # TODO: Scale the data using StandardScaler.
    # TODO: Train a LogisticRegression model with penalty='l2'.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)

    reg_model_l2 = LogisticRegression(penalty='l2', random_state=42, max_iter=2000)
    reg_model_l2.fit(X_train_scaled, y_train)
    
    return reg_model_l2


def apply_l1_regularization(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series) -> LogisticRegression:
    """
    Apply L1 regularization (Lasso) using Logistic Regression.
    
    Returns:
        LogisticRegression: The trained L1 regularized model.
    """
    # TODO: Scale the data using StandardScaler.
    # TODO: Train a LogisticRegression model with penalty='l1' and solver='saga'.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)

    reg_model_l1 = LogisticRegression(penalty='l1', solver='saga', random_state=42, max_iter=2000)
    reg_model_l1.fit(X_train_scaled, y_train)
    
    return reg_model_l1


# --- Main Execution Block (for testing/demo purposes) ---
if __name__ == '__main__':
    # TODO: Make sure 'dataset.csv' exists in your working directory.
    file_path = 'dataset.csv'
    
    # Step 1: Load dataset
    df = pd.read_csv(file_path)
    
    # Step 2: Preprocess data
    X = select_features(df)
    X = handle_missing_values(X)
    X = encode_categorical_features(X)
    y = df['Target']  # TODO: Ensure 'Target' is the correct column for the output labels
    
    # Step 3: Train-test split
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Step 4: Train Decision Tree and evaluate
    model = train_decision_tree(X_train, y_train)
    accuracy, cm = evaluate_model(model, X_test, y_test)
    print("\nDecision Tree Model Accuracy: ", accuracy)
    print("\nConfusion Matrix:\n", cm)
    
    # Step 5: L2 Regularization
    reg_model_l2 = apply_l2_regularization(X_train, y_train, X_test, y_test)
    accuracy_l2 = reg_model_l2.score(X_test, y_test)
    print("\nL2 Regularized Model Accuracy (Ridge): ", accuracy_l2)
    
    # Step 6: L1 Regularization
    reg_model_l1 = apply_l1_regularization(X_train, y_train, X_test, y_test)
    accuracy_l1 = reg_model_l1.score(X_test, y_test)
    print("\nL1 Regularized Model Accuracy (Lasso): ", accuracy_l1)
