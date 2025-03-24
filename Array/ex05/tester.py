from load_image import ft_load
from pimp_image import ft_invert
import numpy as np
from PIL import Image

img = ft_load("landscape.jpg")
array = ft_invert(img)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
print(ft_invert.__doc__)
