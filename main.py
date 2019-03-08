import cv2 as cv
from export_data import readImage
import numpy
from normalization import normalize

# Image read
img = cv.imread("photos/foto2.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)

result, temp, contours, answers = readImage(img)

answers = normalize(answers, 60)

# Sort all Y

for item in answers:
    item.sort(key=lambda x: x[1])

answers.sort(key=lambda x: x[0][1])

for item in answers:
    print(item)

cv.imwrite("results/result.jpg", result)
cv.imwrite("results/result_tmp.jpg", temp)


