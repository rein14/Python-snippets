from get_seasons import get_season
"""main fucntion to compute"""

def main():
    """main function"""
    day = int(input('enter day: '))
    month = str(input('enter month: '))
    print(get_season(month, day))

if __name__ == "__main__":
    main()
