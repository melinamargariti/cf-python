"""Prints Hello Coding"""

def main():
    """main function prints Hello Coding"""
    print("Hello Coding!")

# When we execute this file directly,
# __name__ has the value "__main__".
# If the file is being imported as a module,
# __name__ will be the module's name.
# If the file is being executed directly,
# call function main().
if __name__ == "__main__":
    main()