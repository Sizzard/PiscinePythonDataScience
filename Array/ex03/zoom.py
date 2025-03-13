import numpy as np
from PIL import Image
from load_image import ft_load

def slice_me(family: list, start: int, end: int) -> list:
    """function that takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided
    start and end arguments"""
    try:
        res = np.array(family)[start:end]
        print(f"My new shape is : ({len(res)}, {len(res[0])})")
        return res
    except Exception as e:
        print(e)

def ft_zoom(path: str):
    """function that zoom on a given image file"""
    data = ft_load(path)

    sliced = slice_me(data, 0, 384000)

    # print(sliced)

    arr = np.reshape(sliced, (500,768))

    print(arr)

    im = Image.fromarray(arr)

    im.show()

def main():
    ft_zoom("animal.jpeg")


if __name__ == "__main__":
    main()
