import cv2
import matplotlib as plt

img = cv2.imread('./img/1.jpg')

histb = cv2.calcHist([img], [0], None, [256], [0, 255])
histg = cv2.calcHist([img], [1], None, [256], [0, 255])
histr = cv2.calcHist([img], [2], None, [256], [0, 255])
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')


cv2.waitKey(0)
cv2.destroyAllWindows()