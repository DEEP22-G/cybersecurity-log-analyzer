# Simple Security Log Analyzer

logs = [
    "Login successful",
    "Login failed",
    "Login failed",
    "Login successful",
    "Login failed"
]

failed_attempts = logs.count("Login failed")

print("Security Log Analysis")
print("Total log entries:", len(logs))
print("Failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("Warning: Multiple failed login attempts detected.")
