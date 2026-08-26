import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    # TODO: read the csv into a dataframe
    df = 
    return df


def explore_data(df: pd.DataFrame):
    """
    Perform basic data exploration, printing key details about the dataset.

    Args:
        df (pd.DataFrame): The DataFrame to explore.
    """
    # TODO: Print dataset shape
    # TODO: Print data types of each column
    # TODO: Print number of missing values
    # TODO: Print value counts for key categorical columns (e.g., 'Gender', 'Course','Tuition fees up to date', 'Debtor' etc.)


def create_approval_rate(df: pd.DataFrame):
    """
    Create the 'approval_rate' feature based on 'Curricular units 1st sem (approved)' and 'Curricular units 1st sem (enrolled)' columns.

    Args:
        df (pd.DataFrame): The DataFrame with student data.

    Returns:
        pd.DataFrame: DataFrame with the 'approval_rate' column.
    """
    # TODO: Create 'approval_rate' column by dividing 'Curricular units 1st sem (approved)' by 'Curricular units 1st sem (enrolled)'
    
    return df


def create_performance_score(df: pd.DataFrame):
    """
    Create the 'performance_score' feature based on 'Curricular units 1st sem (approved)' and 'Curricular units 1st sem (evaluations)' columns.

    Args:
        df (pd.DataFrame): The DataFrame with student data.

    Returns:
        pd.DataFrame: DataFrame with the 'performance_score' column.
    """
    # TODO: Create 'approval_rate' column by dividing 'Curricular units 1st sem (approved)' by ''Curricular units 1st sem (evaluations)''
    
    return df


def create_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create all engineered features needed for the analysis.

    Args:
        df (pd.DataFrame): The DataFrame with student data.

    Returns:
        pd.DataFrame: DataFrame with engineered features.
    """
    # TODO: Add engineered features by calling the functions to create 'approval_rate' and 'performance_score'
    df = 
    df = 
    
    # TODO: Print the first few rows of the DataFrame to verify that the new columns are correctly added('Course', 'Gender', 'approval_rate', 'performance_score')
    print("\nData with new columns: ")
    
    
    return df


# --- Main Execution Block ---
if __name__ == '__main__':
    # Path to the dataset
    file_path = 'dataset.csv'
    
    
    df = load_data(file_path)
    
    
    explore_data(df)
    
    
    df = create_engineered_features(df)
