#testing auto run of action based on merge 16/01
#16/01 - test 2
#directly writing in main
from datetime import datetime
import pytz

# Get Indian Standard Time
ist = pytz.timezone("Asia/Kolkata")
now = datetime.now(ist)

# Format time as HH:MM
time_str = now.strftime("%H:%M")

# Extract digits and calculate sum
digit_sum = sum(int(char) for char in time_str if char.isdigit())

# Prepare output text
output = (
    f"Current Indian Time (IST): {time_str}\n"
    f"Sum of digits: {digit_sum}\n"
)

# Write to file
with open("output.txt", "w") as file:
    file.write(output)

print("Output written to output.txt")
print(output)
