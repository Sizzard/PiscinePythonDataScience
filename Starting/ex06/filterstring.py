import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        try:
            nb = int(sys.argv[2])
        except Exception:
            raise AssertionError("AssertionError: the arguments are bad")
        nb = int(sys.argv[2])
        s = sys.argv[1]
        lst = s.split()
        for string in lst:
            if not string.isalnum():
                raise AssertionError("AssertionError: the arguments are bad")
        filtered = ft_filter(lambda s: len(s) > nb, lst)
        filtered = list(filtered)
        print(filtered)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
