from datetime import datetime  #import datetime for working with date and time objects
from zoneinfo import ZoneInfo  #import ZoneInfo for timezone handling
from data.storage import TIMEZONES  #import predefined list of valid timezones
from datetime import datetime, timedelta

def choose_timezone():
    """

    Allow the user to select a valid timezone from a predefined list from storage.
    If the input is invalid (>= 25), prompt the user to try again.
"""

    while True:
        print("Available timezones:")
        for i, tz in enumerate(TIMEZONES, 1):
            print(f"{i}. {tz}")

        try:
            choice = int(input("Select a timezone by entering its number: "))
            if choice >= 25:
                print("Invalid choice. Please select a timezone from the list below.")
                continue  # Retry the selection process
            if 1 <= choice <= len(TIMEZONES):
                selected_timezone = TIMEZONES[choice - 1]
                print(f"You have selected: {selected_timezone}")
                return selected_timezone
            else:
                print("Invalid choice. Please select a timezone from the list below.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Helper function to calculate UTC offset in hours
def get_timezone_offset(timezone):
    timezone_offsets = {
        "UTC": 0,
        "Europe/Bucharest": 2,  # Hardcode Bucharest's offset from UTC (adjust for daylight saving if necessary)
        "Europe/London": 0,  # Example for London; adjust as needed
        "America/New_York": -5,
        # Add other timezones as needed
    }
    return timezone_offsets.get(timezone, 0)  # Default to UTC if timezone is unknown

def convert_to_timezone(date_str, from_timezone, to_timezone):
    """
    Converts a naive datetime string from one timezone to another.
    :param date_str: The date and time in "YYYY-MM-DD HH:MM" format
    :param from_timezone: Original timezone of the datetime
    :param to_timezone: Target timezone for conversion
    :return: Converted datetime string in the target timezone
    """
    try:
        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")  # Parse datetime
        from_offset = get_timezone_offset(from_timezone)  # Get offset for original timezone
        to_offset = get_timezone_offset(to_timezone)  # Get offset for target timezone
        offset_diff = to_offset - from_offset  # Calculate the time difference in hours
        converted_datetime = naive_datetime + timedelta(hours=offset_diff)  # Apply the offset difference
        return converted_datetime.strftime("%Y-%m-%d %H:%M")  # Return as formatted string
    except Exception as e:
        print(f"Error in timezone conversion: {e}")
        return None