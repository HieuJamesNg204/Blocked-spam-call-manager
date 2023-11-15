from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        # Parse the date strings into datetime objects
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')

        # Compare the dates
        if date1 < date2:
            return f"{date_str1} is before {date_str2}"
        elif date1 > date2:
            return f"{date_str1} is after {date_str2}"
        else:
            return f"{date_str1} is the same as {date_str2}"

    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."

# Example usage
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

result = compare_dates(date_str1, date_str2)
print(result)