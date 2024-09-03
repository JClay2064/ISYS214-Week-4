
def is_year_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12 or year < 1:
        return None
    
    # List of days in each month for a common year
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap years
    if month == 2 and is_year_leap(year):
        return 29
    
    return days_in_months[month - 1]

# Testing the function with various test cases
test_cases = [
    (2020, 2),  # Leap year, February
    (2019, 2),  # Common year, February
    (2021, 4),  # April
    (2021, 11), # November
    (2021, 13), # Invalid month
    (-1, 5),    # Invalid year
    (2021, 0)   # Invalid month
]

for year, month in test_cases:
    print(f"Year: {year}, Month: {month} -> Days: {days_in_month(year, month)}")