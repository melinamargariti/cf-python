"""Convert hours to minutes and seconds."""

MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main() -> None:
    """Reads a number of hours from the user and
    prints the equivalent number of minutes and seconds."""

    # Data input
    hours = int(input("Enter hours: "))

    #Processing: Convert hours to minutes and seconds
    minutes = hours * MINUTES_PER_HOUR
    seconds = minutes * SECONDS_PER_MINUTE

    # Print Results
    print(f"{hours} hours is equal to {minutes} minutes or {seconds} seconds.")

if __name__ == "__main__":
    main()