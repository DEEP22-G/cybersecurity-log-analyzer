# cybersecurity-log-analyzer
A simple Python tool for checking failed login attempts in security logs.

## Log Analyzer

This project includes a simple Python script that checks login records.

### How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run: python log_analyzer.py

### Features

- Counts total login records.
- Counts failed login attempts.
- Displays a warning when three or more failed logins are detected.

### Testing

The script was tested using five sample login records.
It correctly identified three failed login attempts and displayed a warning.
