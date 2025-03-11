import sys


def get_morse_code() -> dict:
    """function that returns the morse code in a dict"""
    morse = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    return morse

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        string = sys.argv[1]
        if not string.isalnum():
            raise AssertionError("AssertionError: the arguments are bad")
        morse = get_morse_code()
        for char in string:
            print(f"{morse[char.upper()]}", end="")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()