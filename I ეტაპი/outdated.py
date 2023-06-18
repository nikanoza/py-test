import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Enter a date in month-day-year format (e.g., 9/8/1636 or September 8, 1636): ")
    mdy_match = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", date_input)
    
    if mdy_match:
        month, day, year = mdy_match.groups()
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            break
    else:
        month_match = re.match(r"(\w+)\s+(\d{1,2}),\s+(\d{4})", date_input)
        if month_match:
            month_name, day, year = month_match.groups()

            if month_name in months:
                month = months.index(month_name) + 1
                day = int(day)
                year = int(year)
                break
    
    print("Invalid date format. Please try again.")

formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
print("Formatted date: " + formatted_date)