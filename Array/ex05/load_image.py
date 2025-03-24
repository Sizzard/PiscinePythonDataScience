from PIL import Image


def ft_load(path: str) -> any:
    """function that loads an image, prints its format, and its pixels
    content in RGB format"""
    try:
        with Image.open(path) as im:
            data = im.getdata()
            print(f"The shape of image is: ({im.size[1]}, {im.size[0]}"
                  f", {len(im.getbands())})")
            return data
    except Exception as e:
        print(e)
