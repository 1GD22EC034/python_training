from datetime import datetime
dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
today = datetime.today()
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1
print(f"You are {age} years old.")
