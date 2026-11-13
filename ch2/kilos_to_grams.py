"""Convert kilograms to grams."""

GRAMS_PER_KILO = 1000

def main() -> None:
    """Reads a number of kilograms from the user and
    prints the equivalent number of grams."""

    # Data input
    kilos = int(input("Enter kilograms: "))

    # Processing: Convert kilograms to grams
    grams = kilos * GRAMS_PER_KILO

    # Print Results
    print(f"{kilos} kilograms is equal to {grams} grams.")

if __name__ == "__main__":
    main()