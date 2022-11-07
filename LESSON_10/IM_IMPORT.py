"""
from matplotlib import pyplot as plt


img = plt.imread('A_380.jpg')
plt.imshow(img)
plt.show()

# ДЛЯ КОНСОЛИ
import os
os.system("A_380.jpg")
"""
from PIL import Image
#...
img = Image.open(r'A_380.jpg')
img.show()

