# opencv-math-expression-separator
Given an image of a math-expression, this program aims to separate that into its individual terms. This is what that means:

![sample](https://github.com/utkarsh-21st/math-expression-seperator/blob/master/sample_results/sample1.jpg "sample") ![sample](https://github.com/utkarsh-21st/math-expression-seperator/blob/master/sample_results/sample2.jpg "sample")
![sample](https://github.com/utkarsh-21st/math-expression-seperator/blob/master/sample_results/sample3.jpg "sample")

It works fine so long as the terms are distinctly partitioned, that is to say that it cannot separate a term if it is connected to any other part.
I originally began this project with the aim to design a model which could read hand-written math-expression but later I jettisoned the idea.
If you are interested to continue to do so, here are some datasets that you could train you model on:
- [HASYv2 Dataset](https://www.kaggle.com/martinthoma/hasyv2-dataset-friend-of-mnist "HASYv2 Dataset")
- [CROHME: Competition on Recognition of Online Handwritten Mathematical Expressions](http://www.iapr-tc11.org/mediawiki/index.php/CROHME:_Competition_on_Recognition_of_Online_Handwritten_Mathematical_Expressions "CROHME: Competition on Recognition of Online Handwritten Mathematical Expressions")
