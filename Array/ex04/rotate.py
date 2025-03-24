from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math


def ft_transpose(array: np.array) -> np.array:
    """
    function to transpose the given array
    """
    size = math.isqrt(array.size)
    array = array.reshape(size, size)
    final = np.zeros((size, size), dtype=np.uint8)
    for x, row in enumerate(array):
        # print(x, row)
        for y, nb in enumerate(row):
            # print(nb)
            # print(y)
            final[x][y] = array[y][len(row) - x - 1]
    return final


def ft_rotate(path: str):
    """
    function to rotate a given image file
    """
    try:
        img = ft_load(path)
        data = np.array(img)
        # array = array.reshape(5, 5)
        print(f"Array to begin with : \n{data}")
        data = ft_transpose(data)
        print(f"Array after : \n{data}")
        image = Image.fromarray(data, mode="L")
        plt.imshow(image, cmap='gray', vmin=0, vmax=255)
        plt.show()
    except Exception as e:
        print(e)


def main():
    ft_rotate("animal.jpeg")


if __name__ == "__main__":
    main()
