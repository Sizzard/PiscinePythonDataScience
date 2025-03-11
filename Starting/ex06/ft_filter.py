# def check(letter):
#     """Test function"""
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#     if letter in vowels:
#         return True
#     return False

def ft_filter(function, iterable_object):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is not None:
        return (item for item in iterable_object if function(item))
    else:
        return (item for item in iterable_object if item)


# def main():
#     letters = ['q', 'w', 'e', 'r', 't', False, 'u', 'i', 'o', 'p']
#     filtered = ft_filter(None, letters)
#     print(type(filtered))
#     filtered = list(filtered)
#     print(filtered)


# if __name__ == "__main__":
#     main()
