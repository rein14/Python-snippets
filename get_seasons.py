"""get seasons funcctions"""
def get_season(month, day) -> str:
    """seasons in a year"""

    seasons = {
        "spring": ["March", "April", "May", "June"],
        "summer": ["June", "July", "August", "September"],
        "fall": ["September", "October", "November", "December"],
        "winter": ["December", "January", "February", "March"],
    }
    results = None
    for key, value in seasons.items():
        if month in value:
            if month == "March" and day >= 21:
                results = "its " + key
    return results #ignore errors