# 🧾 Log Analyzer

## 📌 Overview

This project is a lightweight and effective **log analysis tool** built using **Python** and **pandas**. It reads system/application logs from a CSV file and allows users to:

- Count logs based on severity levels
- Filter logs within a specific time range
- Display a set of log entries for quick inspection

This tool is particularly useful for developers, IT administrators, and cybersecurity analysts looking to analyze logs efficiently in a structured and automated manner.

---

## 🚀 Features

- **🔢 Count Logs by Severity Level**  
  View the number of logs classified under levels such as *Information*, *Warning*, and *Error*.

- **🕒 Filter Logs by Time Range**  
  Define a custom time window to isolate logs that occurred during that specific period.

- **👀 Display Logs**  
  Display the first `n` logs from the dataset to quickly inspect log content and structure.

---

## 📁 Input CSV Format

Your CSV log file should contain the following headers:
"Message", "Id", "Version", "Qualifiers", "Level", "Task", "Opcode",
"Keywords", "RecordId", "ProviderName", "ProviderId", "LogName",
"ProcessId", "ThreadId", "MachineName", "UserId", "TimeCreated",
"ActivityId", "RelatedActivityId", "ContainerLog", "MatchedQueryIds",
"Bookmark", "LevelDisplayName", "OpcodeDisplayName", "TaskDisplayName",
"KeywordsDisplayNames", "Properties"


> 🔔 **Note:** A sample log file is not included. Ensure that your CSV follows the above structure.

---

## 🧪 How to Use

1. **Prepare Your Log File**  
   Ensure your log data is saved in a `.csv` file with the above-mentioned headers.

2. **Update the File Path**  
   In the Python script (`log_analyzer.py`), modify the `csv_path` variable to point to your CSV file location.

3. **Run the Script**
```bash
python log_analyzer.py
```
This will:

Count logs by severity level

Filter logs by the date range specified in the code

Display the first 10 (or n) logs for review

💻 Requirements
Python 3.x

pandas

datetime (built-in)

Install the required dependencies using pip:

```bash
pip install pandas
