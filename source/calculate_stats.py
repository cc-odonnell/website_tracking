# this file holds all of the read events functions

from datetime import datetime, timedelta
import pandas as pd


def get_views_last_24hr(views_df):
    "doc string here"
    count_views = len(views_df)
    return count_views

def get_demos_last_24hr(book_demo_df):
    "doc string here"
    count_demos = len(book_demo_df)
    return count_demos


# I changed this so that you have to specify the dataframe as a parameter
def moving_average_views(df, duration):
    """  Returns a list of (hour, 6-hour moving average) pairs for the last `duration` hours. """
    if duration > 18:
        raise ValueError("Duration cannot exceed 18 hours due to 24-hour data retention limit.")

    # Count views per hour
    df['hour'] = df['timestamp'].dt.hour
    hourly_counts = df.groupby("hour").size().reset_index(name = "views")

    result = []

    for i in range(duration):
        end_time = hourly_counts.index[-1 - i]
        start_time = end_time - 5
        window = hourly_counts[(hourly_counts['hour'] > start_time) & (hourly_counts['hour'] <= end_time)]
        avg_views = window.mean()
        result.append((start_time, end_time, avg_views))

    return result


# This function is more general than the function above and should replace it entirely
def moving_average_views_query(df, duration, attribute_filter=None):
    """ Returns a list of (start_hour, end_hour, 6-hour moving average of views)
    Optionally filters to users with a specific attribute set to True.
    """

    if duration > 18:
        raise ValueError("Duration cannot exceed 18 hours due to 24-hour data retention limit.")

    # Ensure timestamp is datetime and round to hour
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.floor('H')

    # Optional filtering
    if attribute_filter:
        attr_name, expected_value = attribute_filter
        df = df[df[attr_name] == expected_value]

    # Count views per hour
    hourly_counts = df.groupby('hour').size().reset_index(name='views')
    hourly_counts = hourly_counts.sort_values('hour').reset_index(drop=True)

    result = []

    for i in range(duration):
        end_idx = len(hourly_counts) - 1 - i
        end_time = hourly_counts['hour'].iloc[end_idx]
        start_time = end_time - timedelta(hours=5)

        window = hourly_counts[
            (hourly_counts['hour'] >= start_time) &
            (hourly_counts['hour'] <= end_time)
        ]

        avg_views = window['views'].mean()
        result.append((start_time, end_time, avg_views))

    result_df = pd.DataFrame(result, columns=["start_hour", "end_hour", "avg_views"])

    return result_df
