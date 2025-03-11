def ft_tqdm(lst: range) -> None:
    """function like tqdm but shittier"""
    length = len(lst)
    for i, _ in enumerate(lst):
        p = i*100/length
        b = int(i*65/length)
        print('\r', end="")
        print(" %d%%|%-65s| %d/%d" % (p, '█'*b, i, length), end="")
        print(end="", flush=True)
        yield
    print('\r', end="")
    print("100%%|%-64s| %d/%d" % ('█'*int(i*66/length), i+1, length), end="")
    print(end="", flush=True)
    yield
