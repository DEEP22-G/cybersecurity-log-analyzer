with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

failed_attempts = 0

for log in logs:
    if log.strip().startswith("FAILED"):
        failed_attempts += 1

print("Security Log Analysis")
print("Total log entries:", len(logs))
print("Failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("Warning: Multiple failed login attempts detected.")