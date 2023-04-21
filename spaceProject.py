import cv2
import numpy as np

def find_stars_in_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # For each pixel, the same threshold value is applied.
    # If the pixel value is less than the threshold, it is set to 0, otherwise it is set to a maximum value.
    # Apply a threshold to identify bright pixels (stars)
    # Inevitably if we found a star in the requested range we necessarily turned it white and everything that is not a star black - background
    _, thresh = cv2.threshold(gray, 209, 255, cv2.THRESH_BINARY)
    # Apply a Gaussian blur to reduce noise
    # makes the noises more uniform Effective in reducing noise the most
    blur = cv2.GaussianBlur(thresh, (5, 5), 0)
    # Find the contours of the stars
    contours, _ = cv2.findContours(blur, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # Iterate over each contour and extract the centroid (x, y) and area (radius)
    starsImag = []
    for contour in contours:
        # area represents the area of the circular region - calculated as np.pi * radius ** 2.
        area = cv2.contourArea(contour)
        if area > 15:  # Filter out small noise
            moments = cv2.moments(contour)
            # makes an average Weighted in he discovers the star center for x and y.
            center_x = int(moments['m10'] / moments['m00'])
            center_y = int(moments['m01'] / moments['m00'])
            radius = int(np.sqrt(area / np.pi))
            brightness =max(img[center_y, center_x])
            starsImag.append((center_x, center_y, radius, brightness))

    # Print the coordinates and brightness values of each star
    print(image_path , ": ")
    i = 1;
    for star in starsImag:
        print("Star {} at (x={}, y={}) with radius={} and brightness={}".format(i, starsImag[0], starsImag[1], starsImag[2], starsImag[3]))
        i += 1
    return starsImag


def find_common_stars(image_path1, image_path2):
    # Find the stars in each image
    stars_image_path1 = find_stars_in_image(image_path1)
    stars_image_path2 = find_stars_in_image(image_path2)

    # take x and y coordinates of stars in each image
    pos1 = np.array([(s[0], s[1]) for s in stars_image_path1])
    pos2 = np.array([(s[0], s[1]) for s in stars_image_path2])

    # Find the overlapping stars using RANSAC idea :
    inliers = []
    for i in range(min(len(stars_image_path1), len(stars_image_path2))):
        # The goal is to calculate a distance,
        # we will initially subtract the position of x1,y1 from the array
        # to get an array of vectors that point from each star in the array to the current star we are looking at.
        # We will want to square up and take the square root to get the resulting distance
        # and make sure it will be positive and not negative and add up the result.
        # The resulting distance is stored in a new array.
        x1, y1 = stars_image_path1[i][0], stars_image_path1[i][1]
        dists1 = np.sqrt(np.sum((pos1 - np.array([x1, y1])) ** 2, axis=1))
        dists2 = np.sqrt(np.sum((pos2 - np.array([x1, y1])) ** 2, axis=1))
        # We would like to find the closest star to the current star.
        # Therefore we would like to take the minimum number from the array
        id_star1 = np.argmin(dists1)
        id_star2 = np.argmin(dists2)

        # Set the threshold for RANSAC
        # and if it really is a overlapping star we will add it to the list of common stars
        if abs(dists1[id_star1]-dists2[id_star2]) < 200:
            inliers.append((stars_image_path1[i], stars_image_path2[i]))

    # Print the number of overlapping stars and their positions
    print("Number of overlapping stars: ", len(inliers))
    for i, inlier in enumerate(inliers):
        print("imag 1 star : ({}, {}) with imag 2 star : ({}, {})".format(inlier[0][0], inlier[0][1], inlier[1][0], inlier[1][1]))

