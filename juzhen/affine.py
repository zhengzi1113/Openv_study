import cv2
import numpy as np

img =  cv2.imread('/home/xiang/OpenCV/img/2.jpg')
h, w, ch = img.shape

# M = np.float32([[1, 0, 100], [0, 1, 0]])

# M = cv2.getRotationMatrix2D((30,100), 30, 1.2)

src = np.float32([[10,10], [10, 130], [80,20]])
dst = np.float32([[20,40], [40, 100], [100,10]])
M = cv2.getAffineTransform(src, dst)

new = cv2.warpAffine(img, M, (w,h))

cv2.imshow("img", img)
cv2.imshow("new", new)
cv2.waitKey(0)
cv2.destroyAllWindows()