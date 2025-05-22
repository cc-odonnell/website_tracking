# example tests to catch silent errors
# missing values, strings coercible to timestamps, cardinality
# categorical variables have all known values

import pandas as pd
from inputs import variable_req

# variable req file would look something like this...
# list of expected values for key variables in the dataset

expected_column_values = {
    "event_type": ['pricing_page', 'form_submit',
                   'demo_click', 'whitepaper_download',
                   'page_view', 'scroll', 'click', 'exit'],
    "persona_type": ['researcher', 'buyer_intent', 'curious', 'demo_seeker']
}

# data checks

def validate_var_names(df: pd.DataFrame, required_columns=None):
    """Ensure all required columns are present."""
    if required_columns is None:
        required_columns = ['user_id', 'event_type', 'timestamp']
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return {'Columns': df.columns.tolist()}


def check_nulls(df: pd.DataFrame):
    """Check for missing values in all columns."""
    print(f" non null values: {df.count().to_dict()}")
    nulls = df.isnull().sum()
    if nulls.any():
        raise ValueError(f"Null values found in: {nulls[nulls > 0].to_dict()}")
    return "No null values"


def check_timestamp_format(df: pd.DataFrame, column='timestamp'):
    """Ensure timestamps are parseable."""
    try:
        pd.to_datetime(df[column])
    except Exception as e:
        raise ValueError(f"Timestamp parsing failed: {e}")
    return "Timestamp parseable"



def check_cardinality(df: pd.DataFrame, column: str, expected_values: list = None, max_unique: int = 10):
    """ Checks that the specified column has reasonable cardinality. """
    unique_vals = df[column].dropna().unique()
    n_unique = len(unique_vals)

    print(f"Column '{column}' has {n_unique} unique values: {list(unique_vals)}")

    if n_unique > max_unique:
        raise ValueError(f"Cardinality too high for '{column}': {n_unique} unique values (max allowed = {max_unique})")

    if expected_values:
        unexpected = set(unique_vals) - set(expected_values)
        if unexpected:
            raise ValueError(f"Unexpected values in '{column}': {unexpected}")

    return "No column has more than 10 (or max_unique) values"


def check_column_values(df: pd.DataFrame, column: str, allowed_values: list):
    """ Checks whether a column contains unexpected values not listed in allowed_values. """
    actual_values = set(df[column].unique())
    unexpected_values = actual_values - set(allowed_values)

    if unexpected_values:
        raise ValueError(f"Unexpected values found in '{column}': {unexpected_values}")

    print(f"All values in '{column}' are within expected range.")


def run_all_value_checks(df: pd.DataFrame):
    """ Iterates over all required columns and runs value checks."""
    for column, allowed_values in variable_req.expected_column_values.items():
        try:
            check_column_values(df, column, allowed_values)
        except ValueError as e:
            print(f"{e}")


