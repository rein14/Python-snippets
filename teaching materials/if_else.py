def get_season(month, day) -> None:
    """seasons in a year"""

    seasons = {
        "spring": ["March", "April", "May", "June"],
        "summer": ["June", "July", "August", "September"],
        "fall": ["September", "October", "November", "December"],
        "winter": ["December", "January", "February", "March"],
    }

    for key, value in seasons.items():
        if month in value:
            if month == "December" and day >= 21:
                print("its winter")
    return


print(get_season("December", 21))
