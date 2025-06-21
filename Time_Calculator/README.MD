# ⏰ Time Calculator

A Python function `add_time` that takes a starting time, a duration, and optionally a starting day of the week, and returns the new time after the duration has been added.

---

## 📌 Features

- Handles 12-hour clock format with AM/PM.
- Calculates time correctly across day boundaries.
- Displays `(next day)` or `(n days later)` as needed.
- Optionally computes the new day of the week.
- Returns output in a clean, readable format.

---

## 🧮 Function Signature

```python
add_time(start: str, duration: str, day: Optional[str] = None) -> str
Parameters:
start (str): Start time in format "HH:MM AM/PM", e.g., '3:00 PM'

duration (str): Duration to add in "H:MM" format, e.g., '3:10'

day (str, optional): Starting day of the week, case insensitive, e.g., 'Monday'

✅ Example Usage

print(add_time('3:00 PM', '3:10'))
# ➤ 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# ➤ 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# ➤ 12:03 PM

print(add_time('10:10 PM', '3:30'))
# ➤ 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# ➤ 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# ➤ 7:42 AM (9 days later)

📦 Project Structure

time_calculator/
│
├── main.py           # Contains the add_time function and sample calls
└── README.md         # This file
📚 How It Works
Converts 12-hour format to 24-hour for easy math

Adds hours and minutes, tracks overflow

Computes how many days have passed

Adjusts and formats the result into a readable 12-hour time

Computes the resulting day (if provided)

🚫 Limitations
Assumes valid input format (start and duration)

Duration minutes must be less than 60

No built-in input validation

🔧 Requirements
Python 3

No external libraries needed

📜 License
This project is open-source and free to use under the MIT License.

👤 Author
Abhishek Anand
Passionate about clean and readable Python code 🐍
