# OpenCV Card Scanner

### Description:

Simple project detecting answers selected on specific Exam Cards based on Photo/Scan.
Script was manually tested on examples available in `./photos/` catalogue with 100% efficiency.
It's structured as it is, because it was supposed to be module for another project.

### How to run

To run script simply run:

```
$ git clone https://github.com/MikusRy/scanner.git
$ cd scanner/
$ python3 main.py
```
Script will automatically evaluate cards existing in `./photos/` and save results to `./results/` catalogue.
You will find there 3 files:
* Photo after threshold (Black & White).
* Photo after processing with detected objects framed using red colour.
* JSON file with exported answers.

### How it works:
Script uses openCV to open, process and detect squares on `.jpg` files stored in `./photos/` catalogue.
After object detection, structure detection and denoising part kicks in. 

```
Process of answer detection is strongly bound with structure of Exam Card and 
won't work for any other type of card, until reprogrammed.
```

What script really does is detecting not selected fields, 
since it's easier to say which fields are missing `(selected ones are treated as missing)`, 
than looking only for selected ones and trying to guess where do these belong.


### Recommendations

If you're interested in using this script, below you can find list of best practises which will 
decrease chance of failure:

* While taking photo of exam card try to focus as much as you can on card. 
It's height should be at least 70% of the photo's height.
* Try to avoid using light colours while selecting fields `(Black and blue colours are best for this)`.
* Watch out for your camera flash, overlighting your photo might cause mistakes during evaluation process.
