# opencv-math-expression-separator
Given an image of a math-expression, this program aims to separate that into its individual terms. This is what that means:

![sample](https://github.com/utkarsh-21st/math-expression-seperator/blob/master/sample_results/sample1.jpg "sample") ![sample](https://github.com/utkarsh-21st/math-expression-seperator/blob/master/sample_results/sample2.jpg "sample")
![sample](https://github.com/utkarsh-21st/math-expression-seperator/blob/master/sample_results/sample3.jpg "sample")

How to run?
```shell
git clone git@github.com:utkarsh-21st/math-expression-seperator.git
cd math-expression-seperator
python main -i input_path -o output_path --show_boxes
```
- input_path -> image path
- output_path -> path where the results will get saved
- --show_boxes is an optional argument


### Overview:
First, the program reads the image in gray-scale, resized to a width of 600 while maintaining the aspect ratio, followed by OpenCV [Adaptive Thresholding](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html "Adaptive Threshold"). Then, it finds contours using OpenCV [findContours](https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a "findContours") function, filtering out irrelevant contours (or noise) based on their areas. [Contours](https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html "Contours") here captures the outline of each term. Using contours we extract each term from the image and save the results. 
The program can separate any abstract into its individual terms.

It works fine so long as the terms are distinctly partitioned, which is to say that it cannot separate a term if it is connected to any other part.
I originally began this project intending to design a model that could read hand-written math-expression but later I discarded the idea.
If you are interested to continue to do so, here are some datasets that you could train your model on:
- [HASYv2 Dataset](https://www.kaggle.com/martinthoma/hasyv2-dataset-friend-of-mnist "HASYv2 Dataset")
- [Handwritten math symbols dataset](https://www.kaggle.com/xainano/handwrittenmathsymbols "Handwritten math symbols dataset")
- [CROHME: Competition on Recognition of Online Handwritten Mathematical Expressions](http://www.iapr-tc11.org/mediawiki/index.php/CROHME:_Competition_on_Recognition_of_Online_Handwritten_Mathematical_Expressions "CROHME: Competition on Recognition of Online Handwritten Mathematical Expressions")
