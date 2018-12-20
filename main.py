import cv2 as cv
from export_data import readImage
import numpy

# Image read
img = cv.imread("photos/test.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)

result, temp, contours, answers = readImage(img)

for item in answers:
    print(item)

cv.imwrite("results/result.jpg", result)
cv.imwrite("results/result_tmp.jpg", temp)


