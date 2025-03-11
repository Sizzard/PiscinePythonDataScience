import sys


def ft_is_upper(s: str) -> int:
    """This function check for how many upper
    chars there is in the string provided"""
    counter = 0
    for char in s:
        if char.isupper() is True:
            counter += 1
    return counter


def ft_is_lower(s: str) -> int:
    """This function check for how many lower
    chars there is in the string provided"""
    counter = 0
    for char in s:
        if char.islower() is True:
            counter += 1
    return counter


def ft_is_space(s: str) -> int:
    """This function check for how many space
    chars there is in the string provided"""
    counter = 0
    for char in s:
        if char.isspace() is True:
            counter += 1
    return counter


def ft_is_digit(s: str) -> int:
    """This function check for how many digit
    there is in the string provided"""
    counter = 0
    for char in s:
        if char.isdigit() is True:
            counter += 1
    return counter


def is_punctuation(s: str) -> bool:
    """This function returns a bool whether the char
    provided is a punctuation mark"""
    return (
        s == "." or s == "," or s == "?"
        or s == "!" or s == ";" or s == ":")


def ft_is_punctuation(s: str) -> int:
    """This function check for how many punctuation mark
    there is in the string provided"""
    counter = 0
    for char in s:
        if is_punctuation(char) is True:
            counter += 1
    return counter


def main():
    string = None
    try:
        if len(sys.argv) == 1:
            while string is None or string == "":
                string = input("What is the text to count?\n")
            print("TEST")
        else:
            string = sys.argv[1]
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError : more than\
                one argument provided")
        upper_chars = ft_is_upper(string)
        lower_chars = ft_is_lower(string)
        space_chars = ft_is_space(string)
        digit_chars = ft_is_digit(string)
        punctuation_chars = ft_is_punctuation(string)
        print(f"The text contains {len(string)} characters:")
        print(f"{upper_chars} upper letters")
        print(f"{lower_chars} lower letters")
        print(f"{punctuation_chars} punctuation marks")
        print(f"{space_chars} spaces")
        print(f"{digit_chars} digits")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
