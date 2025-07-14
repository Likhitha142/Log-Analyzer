import pandas as pd
from datetime import datetime

# Path to your CSV log file
csv_path = "log.csv"

# Column headers for the log file
columns = [
    "Message", "Id", "Version", "Qualifiers", "Level", "Task", "Opcode", "Keywords",
    "RecordId", "ProviderName", "ProviderId", "LogName", "ProcessId", "ThreadId",
    "MachineName", "UserId", "TimeCreated", "ActivityId", "RelatedActivityId",
    "ContainerLog", "MatchedQueryIds", "Bookmark", "LevelDisplayName",
    "OpcodeDisplayName", "TaskDisplayName", "KeywordsDisplayNames", "Properties"
]

# Load CSV into pandas DataFrame
df = pd.read_csv(csv_path, names=columns, skiprows=2)

# Convert TimeCreated to datetime
df['TimeCreated'] = pd.to_datetime(df['TimeCreated'], errors='coerce')

# Count logs by severity level
def count_logs_by_level(df):
    return df['LevelDisplayName'].value_counts()

# Filter logs within a given time range
def filter_logs_by_time(df, start_time, end_time):
    mask = (df['TimeCreated'] >= start_time) & (df['TimeCreated'] <= end_time)
    return df.loc[mask]

# Display top n rows
def display_logs(df, n=10):
    print(df.head(n))

# Main
if __name__ == "__main__":
    print("Log counts by level:")
    print(count_logs_by_level(df))

    # Example time filter
    start_time = datetime(2023, 1, 1)
    end_time = datetime(2024, 1, 1)

    filtered_logs = filter_logs_by_time(df, start_time, end_time)
    print(f"\nLogs between {start_time} and {end_time}:")
    display_logs(filtered_logs, n=10)
