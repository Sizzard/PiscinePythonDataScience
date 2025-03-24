import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def error_check(lst: list, start: int, end: int):
    """function that raise exception if assertion of type is not ok"""
    if not isinstance(start, int):
        raise AssertionError("Assertion error : not an int")
    if not isinstance(end, int):
        raise AssertionError("Assertion error : not an int")


def slice_me(family: list, start: int, end: int) -> any:
    """function that takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the provided
    start and end arguments"""
    try:
        error_check(family, start, end)
        res = np.array(family)[start:end]
        return res
    except Exception as e:
        print(e)


def ft_zoom(path: str):
    """function that zoom on a given image file"""
    try:
        data = ft_load(path)
        array = np.array(data)
        print(array)
        midX = data.size[0] // 2
        midY = data.size[1] // 2
        zooming = midX
        if midY < midX:
            zooming = midY
        arr = np.zeros(shape=(zooming, zooming, 3), dtype=np.uint8)
        startX = midX - zooming // 2
        startY = midY - zooming // 2

        for idx in range(zooming):
            posBegin = (startY + idx) * data.size[0] + startX
            posEnd = posEnd = posBegin + zooming
            arr[idx] = slice_me(array, posBegin, posEnd)
            # print(f"{posBegin}, {posEnd}")

        final = np.zeros(shape=(zooming, zooming), dtype=np.uint8)
        for x, blocks in enumerate(arr):
            for y, color in enumerate(blocks):
                R = color[0]
                G = color[1]
                B = color[2]
                # l = int(0.2126*R + 0.7152*G + 0.0722*B)
                pix = int(0.299 * R + 0.587 * G + 0.114 * B)
                # print(f"{x}, {y}, = {l}")
                final[x][y] = pix

        print(final.shape)

        image = Image.fromarray(final, mode="L")

        plt.imshow(image, cmap='gray', vmin=0, vmax=255)
        plt.show()

    except Exception as e:
        print(e)


def main():
    ft_zoom("animal.jpeg")


if __name__ == "__main__":
    main()
