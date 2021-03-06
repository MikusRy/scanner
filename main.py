import glob
import json
import os

import cv2 as cv

from app.NumpyEncoder import NumpyEncoder
from app.Results import find, group, evaluate
from app.export_data import readImage

if __name__ == "__main__":
    # Image read
    files = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob("./photos/*.jpg")]
    if not os.path.exists('./results/'):
        os.makedirs('./results')
    for file in files:
        # Read the image
        result, temp, contours, answers, size = readImage(file)
        # Sort all by lines
        for item in answers:
            item.sort(key=lambda x: x[1])
        answers.sort(key=lambda x: x[0][1])
        # final evaluation - served as dictionary
        answers = evaluate(group(find(answers, size), 65), 25)
        # save to json file
        with open('results/{0}.json'.format(file), 'w') as outfile:
            json.dump(answers, cls=NumpyEncoder, indent=4, fp=outfile)

        cv.imwrite("results/{0}.jpg".format(file), result)
        cv.imwrite("results/{0}_tmp.jpg".format(file), temp)
