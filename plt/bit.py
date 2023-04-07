import cv2
import numpy as np

img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)

img[20:80, 20:80] =255
img2[50:150, 50:150] =255
# new = cv2.bitwise_not(img)
# new = cv2.bitwise_and(img, img2)
new = cv2.bitwise_or(img, img2)
# new = cv2.bitwise_xor(img, img2)

cv2.imshow('img', img)
cv2.imshow('img2', img2)

cv2.imshow('new', new)

cv2.waitKey(0)