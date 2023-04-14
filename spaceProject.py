import cv2
import numpy as np

def find_stars_in_image(path):
    # Load the image
    img = cv2.imread(path)
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
    stars = []
    for contour in contours:
        # area represents the area of the circular region - calculated as np.pi * radius ** 2.
        area = cv2.contourArea(contour)
        if area > 15:  # Filter out small noise
            moments = cv2.moments(contour)
            # makes an average Weighted in he discovers the star center for x and y.
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            radius = int(np.sqrt(area / np.pi))
            brightness =max(img[cy, cx])
            stars.append((cx, cy, radius, brightness))

    return stars


def find_common_stars(image_path1, image_path2):
    # Find the stars in each image
    stars1 = find_stars_in_image(image_path1)
    stars2 = find_stars_in_image(image_path2)

    # Compute the positions of the stars in each image
    pos1 = np.array([(s[0], s[1]) for s in stars1])
    pos2 = np.array([(s[0], s[1]) for s in stars2])

    # Find the overlapping stars using RANSAC
    inliers = []
    for i in range(min(len(stars1), len(stars2))):
        # The goal is to calculate a distance :
        # we will initially subtract the position of x1,y1 from the array
        # to get an array of vectors that point from each star in the array to the current star we are looking at.
        # We will want to square up and take the square root to get the resulting distance
        # and make sure it will be positive and not negative and add up the result.
        # The resulting distance is stored in a new array.
        x1, y1 = stars1[i][0], stars1[i][1]
        dists1 = np.sqrt(np.sum((pos1 - np.array([x1, y1])) ** 2, axis=1))
        dists2 = np.sqrt(np.sum((pos2 - np.array([x1, y1])) ** 2, axis=1))
        # We would like to find the closest star to the current star.
        # Therefore we would like to take the minimum number from the array
        idx1 = np.argmin(dists1)
        idx2 = np.argmin(dists2)

        if abs(dists1[idx1]-dists2[idx2]) < 200:  # threshold for RANSAC 
            inliers.append((stars1[i], stars2[i]))

    # Print the overlapping stars and their positions
    print("Number of overlapping stars: ", len(inliers))
    for i, inlier in enumerate(inliers):
        print("imag 1 star : ({}, {}) is overlapping with imag 2 star : ({}, {})".format(inlier[0][0], inlier[0][1], inlier[1][0], inlier[1][1]))
