import time
from datetime import datetime, timezone

current_time = datetime.now(timezone.utc)
print(current_time)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)

start_time_string = "2024-03-04T17:51:00.000Z"
start_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

# Convert the start time string to a time struct
start_time = time.strptime(start_time_string, start_time_format)

# Calculate the time difference in seconds between the current time and the start time
current_time = time.gmtime()
time_difference = time.mktime(start_time) - time.mktime(current_time)

# Wait until the specified start time is reached
time.sleep(time_difference)

# Run your program here
print("Program started at", start_time)