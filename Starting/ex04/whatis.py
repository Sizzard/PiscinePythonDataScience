import sys

try:
    nb = 0
    try:
        nb = int(sys.argv[1])
    except:
        raise AssertionError("AssertionError: argument is not an integer")
    if isinstance(nb, int) is False:
        raise AssertionError("AssertionError: argument is not an integer")
    elif len(sys.argv) > 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(e)