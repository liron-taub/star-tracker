***EX1***

introduction:

In the assignment I used the Paizarm software, in order to run this assignment you need to install the following libraries:
openCV, numpy, cv2

If we want to use the functions, we need to bring them paths to the image.
The code supports jpg, png images.
The function def find_stars_in_image(path): is the second part of the assignment, it receives a path to one image as needed
The function def find_common_stars(image_path1, image_path2): is for the third part of the assignment, receives two paths for two images to be compared between them.
Explanation of the code and the assignment:
 
In this task we were involved in the development of an algorithm for star classification. Given an image of stars,
And given a database of the positions of the stars - we would like to find a match between the stars in the image and those in the database.
The second thing we had to do is that given an image we could identify the stars in the image.
Humans see every "picture" in the world as a range of numbers.
For this task, let's say it's a black and white grayscale image:

![pixel in imag](https://raw.githubusercontent.com/liron-taub/star-tracker/main/%D7%90%D7%99%D7%9A%20%D7%91%D7%A0%D7%99%20%D7%90%D7%93%D7%9D%20%D7%A8%D7%95%D7%90%D7%99%D7%9D%20%D7%A6%D7%91%D7%A2%D7%99%D7%9D.png)

Of course the pictures in real life are not as beautiful and smooth as we would like them to be.
The stars are not necessarily white and the sky is not necessarily black.
We'll want the first step to take the image and every pixel below 206 will be mapped to black, so we'll get an image that's mostly black and smooth contains shades of gray.
After that: we would like to use the algorithms learned in the image processing course such as the Gaussian filter to turn a "dirty" image into a clean image where the stars can be mapped.
A reminder of why this is a Gaussian filter algorithm:
In image editing, a Gaussian filter is used to filter out noise and refine sharp transitions between colors by blurring them, which is why it is also called "Gaussian blur".
In this method, for each pixel in the image the output value of the filter is a weighted average between its color and the colors of its neighbors, where the weights are determined according to the coefficients of the Gaussian distribution (the familiar "normal" distribution shaped like a bell). In this method, when averaging, a maximum weight is given to the current pixel, a smaller weight to its immediate neighbors and a smaller weight to neighbors the further away they are.

After you have managed to map the stars in the image, we will want to save them in some database to use in the third part of the assignment.
in the third part
The function calls the find_stars_in_image function twice, passing both image paths as arguments.
The function then creates two NumPy arrays, pos1 and pos2, containing the (x, y) coordinates of the stars in each image.

The function then initializes an empty list, internally, to hold the overlapping stars.

The function loops through each star in the first image and calculates the distance between that star to all stars in both images using the RANSAC concept.

Introduction to why it is a RANSAC algorithm at all: it is actually a probabilistic algorithm that works in a method
Iterative for estimating parameters of a mathematical model from a data set (in our case points)
contains outliers Therefore, we can use the RANSAC algorithm to calculate transformation parameters between images.
Support (Inliers) - Given a certain mathematical model, the support is defined as the group of points that are at most a certain threshold away from the model. The rest of the points will be considered as exceptions.

In our code this is done by subtracting the (x, y) position of the current star from the arrays pos1 and pos2 to get an array of vectors pointing from each star in the array to the current star we are looking at. Then, the Euclidean distance between the current star and each star in the two images is calculated and stored in the arrays dists1 and dists2, respectively.

The function finds the closest star to the current star by finding the index of the minimum value in the dists1 and dists2 arrays. If the difference between the distances of the closest stars in the two images is less than 200, the current star is considered an overlapping star, and its coordinate values and brightness values in the two images are added to the internal list.

Finally, the function prints the number of overlapping stars and their positions in the two images.

An explanation of what a Euclidean plane is: (taken from Wikipedia, attached link)
The Euclidean plane is a set of points that maintain certain relationships, which can be expressed in terms of distance and angle. For example, there are two basic operations in an airplane. One is copying, that is, moving the plane so that all points on it move in the same direction and at the same distance. The second is a rotation around a fixed point in the plane, so that all the points in the plane will move at the same angle relative to the fixed point. One of the foundations of Euclidean geometry is that two bodies in a plane, i.e. subsets of the plane, are considered equivalent (overlapping) if it is possible to move from one to the other by way of copying, rotations and reflections.
Using the Euclidean width is exactly what we would like to do to find overlapping stars between two images using the Ransack algorithm.
The calculation is done by subtracting the position and taking the Euclidean distance as described in Wikipedia:
[Euclidean distance](https://he.wikipedia.org/wiki/%D7%9E%D7%A8%D7%97%D7%91_%D7%90%D7%95%D7%A7%D7%9C% D7%99%D7%93%D7%99)
