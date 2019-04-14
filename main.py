import glob
import json
import os

import cv2 as cv

from NumpyEncoder import NumpyEncoder
from Results import find, group, evaluate
from export_data import readImage

if __name__ == "__main__":
    # Image read

    files = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob("./photos/*.jpg", recursive=True)]
    if not os.path.exists('./results/'):
        os.makedirs('./results')
    for file in files:
        img = cv.imread("photos/{0}.jpg".format(file), cv.IMREAD_GRAYSCALE)
        img = cv.medianBlur(img, 5)

        result, temp, contours, answers, size = readImage(img)

        # Sort all by lines

        for item in answers:
            item.sort(key=lambda x: x[1])
        answers.sort(key=lambda x: x[0][1])

        # final evaluation - served as dictionary
        answers = evaluate(group(find(answers, size), 65), 25)
        # save to json file
        with open('results/{0}.json'.format(file), 'w') as outfile:
            json.dump(answers, cls=NumpyEncoder, indent=4, fp=outfile)
        # print results
        # print(json.dumps(answers, cls=NumpyEncoder, indent=4))

        cv.imwrite("results/{0}.jpg".format(file), result)
        cv.imwrite("results/{0}_tmp.jpg".format(file), temp)
