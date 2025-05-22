# primary read events function

import pandas as pd
from datetime import datetime, timedelta


# Global in-memory store
views_df = pd.DataFrame()

def track_view(json_blob):
    """ Accepts a JSON blob and keeps only the last 24 hours of data."""

    global views_df

    # Convert blob to DataFrame
    new_df = pd.DataFrame(json_blob)

    # Convert timestamp column from string to datetime
    new_df["timestamp"] = pd.to_datetime(new_df["timestamp"])

    # Append to global views_df
    views_df = pd.concat([views_df, new_df], ignore_index=True)

    # Trim to last 24 hours
    cutoff = datetime.now().replace(minute=0, second=0, microsecond=0) - timedelta(hours=24)
    views_df = views_df[views_df["timestamp"] >= cutoff].reset_index(drop=True)

    return views_df



# comments here

def track_book_demo(df):
    "Accepts a DataFrame and subsets data to book_demo events"

    global views_df

    book_demo_df = views_df[views_df["book_demo"] == True]

    return book_demo_df

