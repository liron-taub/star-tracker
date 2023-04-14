# star-tracker
***EX1***

In this assignment we dealt with the development of an algorithm for classifying stars. Given an image of stars,
And given a database of the positions of the stars - we would like to find a match between the stars in the image and those in the database.
The first thing we had to do is that given an image we would be able to identify the stars in the image.
Humans see every "picture" in the world as a range of numbers.
For the purpose of this assignment, let's assume that this is a black and white grayscale image:
![enter image description here](https://raw.githubusercontent.com/liron-taub/star-tracker/main/%D7%90%D7%99%D7%9A%20%D7%91%D7%A0%D7%99%20%D7%90%D7%93%D7%9D%20%D7%A8%D7%95%D7%90%D7%99%D7%9D%20%D7%A6%D7%91%D7%A2%D7%99%D7%9D.png)

Of course, the pictures in real life are not as nice and smooth pictures as we would like them to be.
The stars are not necessarily white and the sky is not necessarily black.
We would like the first step to take the image and every pixel below 206 will be mapped to be black, so that we get an image that is mostly black and some of it contains shades of gray.
After that: we would like to use the algorithms learned in the image processing course such as the Gaussian filter, which comes to turn a "dirty" image into a clean image in which it is possible to map the stars.
A reminder of what a Gaussian filter algorithm is:
In image editing, a Gaussian filter is used to filter out noise and refine sharp transitions between colors by blurring them, and is therefore also called "gaussian blur".
In this method, for each pixel in the image the filter output value is a weighted average between its color and the colors of its neighbors, with the weights determined according to the coefficients of the Gaussian distribution (the familiar "normal" distribution that is shaped like a bell). In this method, when averaging, a maximum weight is given to the current pixel, a smaller weight to its adjacent neighbors, and a smaller weight to the neighbors the further away they are.

After you have managed to map the stars in the picture, we will want to save them in some database in order to use it in the second part of the assignment.
In order to find stars we wanted to use the idea of the RANSAC algorithm:

The RANSAC algorithm is a probabilistic algorithm that works in a method
iterative for estimating parameters of a mathematical model from a set of data (in our case points)
containing outliers Therefore, we can use the RANSAC algorithm to calculate transformation parameters between images.
Support (inliers) - Given a certain mathematical model, the Support is defined to be the group of points that are at most a certain threshold away from the model. The rest of the points will be considered as the outliers.

We would also like to use another topic which is Euclidean space and Euclidean plane:

The Euclidean plane is a set of points that maintain certain relationships, which can be expressed in terms of distance and angle. For example, there are two basic operations in a plane. One is copying, that is, moving the plane so that all the points on it move in the same direction and the same distance. The other is a rotation around a fixed point in the plane, so that all the points in the plane will move at the same angle relative to the fixed point. One of the foundations of Euclidean geometry is that two bodies in a plane, i.e., subsets of the plane, are considered equivalent (overlapping) if it is possible to move from one to the other by way of copying, rotations and reflections.
Using the Euclidean width is exactly what we would like to do in order to find overlapping stars between two images by using the Ransack algorithm.
The calculation is done by subtracting the position and taking the Euclidean distance as described in Wikipedia:
[Euclidean distance](https://he.wikipedia.org/wiki/%D7%9E%D7%A8%D7%97%D7%91_%D7%90%D7%95%D7%A7%D7%9C%D7%99%D7%93%D7%99)


