import cv2 as cv
import numpy


def getREKT(approx):
    answer_table = []
    answer_temp = []

    for item in approx.ravel():
        answer_temp.append(item)
        if len(answer_temp) == 2:
            answer_table.append(answer_temp)
            answer_temp = []
    return answer_table


def readImage(img):
    # Import image shape data
    height, width = img.shape

    # Image to greyscale convert, contours detection
    threshold = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 255, 13)
    temp = threshold
    _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Image to RGB convert, for colorful contours draw
    threshold = cv.cvtColor(threshold, cv.COLOR_GRAY2RGB)

    answers = []
    for cnt in contours:
        approx = cv.approxPolyDP(cnt, 0.047 * cv.arcLength(cnt, True), True)
        if len(approx) == 4:
            if 100 < approx.ravel()[1] < 4280:
                cv.drawContours(threshold, [approx], -1, (0, 0, 255), 3)

                answers.append(getREKT(approx))

    print("height: " + str(height) + "; Width: " + str(width) + ";")
    return threshold, temp, contours, answers
