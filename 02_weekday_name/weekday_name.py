def weekday_name(day_of_week):
    """Return name of weekday.
    """
    weekday = ['none', 'sunday', 'Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Satruday"]
    if day_of_week == 0 or day_of_week > 7: return "None"
    else: return weekday[day_of_week]

print(weekday_name(7))