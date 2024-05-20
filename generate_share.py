import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

def draw(img, h, w, l, c):
    locate_h = 2 * h
    locate_w = 2 * w
    if l == 0:
        img[locate_h][locate_w] = c
        img[locate_h][locate_w+1] = c
    elif l == 1:
        img[locate_h][locate_w] = c
        img[locate_h+1][locate_w] = c
    elif l == 2:
        img[locate_h][locate_w] = c
        img[locate_h+1][locate_w+1] = c
    elif l == 3:
        img[locate_h+1][locate_w] = c
        img[locate_h+1][locate_w+1] = c
    elif l == 4:
        img[locate_h][locate_w+1] = c
        img[locate_h+1][locate_w+1] = c
    elif l == 5:
        img[locate_h][locate_w+1] = c
        img[locate_h+1][locate_w] = c
    else:
        print("Error: Wrong list")
        exit(1)
    return img

def draw_white(img, h, w, l):
    return draw(img, h, w, l, 0)

def draw_black(img, h, w, l):
    r = np.random.randint(low = 1, high = 6, size = 1)
    l_new = (l + r) % 6
    return draw(img, h, w, l_new, 0)

try:
    imgname = sys.argv[1]
except:
    print("Usage: secret.py FILENAME")
    exit(1)

#画像をグレースケールで読み込む
original = cv2.imread(imgname, cv2.IMREAD_GRAYSCALE)
try:
    height, width = original.shape[:3]
except:
    print("Error: Can't input file")
    exit(1)

#シェア画像のサイズは元の縦横2倍
size = (height*2, width*2)
share1 = np.zeros(size, np.uint8)
share2 = share1 + 255
list = np.random.randint(low = 0, high = 6, size = (height, width))

for h in range(height):
    for w in range(width):
        l = list[h][w]
        share1 = draw(share1, h, w, l, 255)
        if original[h][w] <= 128:
            share2 = draw_white(share2, h, w, l)
        else:
            share2 = draw_black(share2, h, w, l)

cv2.imwrite('share1.jpg', share1)
cv2.imwrite('share2.jpg', share2)

result = (share1 + share2) % 255
"""
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
cv2.imwrite('result.jpg', result)
