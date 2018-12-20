import cv2 as cv


def show(threshold):
    cv.imshow("Shapes", threshold)
    cv.waitKey(0)
    cv.destroyAllWindows()
