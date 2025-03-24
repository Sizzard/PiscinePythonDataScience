import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt

def ft_invert(array) -> np.array:
    """
function to invert colors on given array
    """
    try:
        if type(array) != np.array:
            array = np.array(array)
        array = 255 - array
        array = array.reshape(img.size[1], img.size[0], 3)
        image = Image.fromarray(array, mode="RGB")
        image.show()
        return 255 - array
    except Exception as e:
        print(e)

def main():
    try:
        img = ft_load("landscape.jpg")
        array = np.array(img, dtype=np.uint8)
        print(f"Before invert \n{array}")
        array = ft_invert(array)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
