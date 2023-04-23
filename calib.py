import numpy as np
import cv2

# Define the number of inner corners in the calibration pattern
pattern_size = (9, 6)

# Create the calibration pattern object
calibration_pattern = np.zeros((pattern_size[1]*pattern_size[0], 3), np.float32)
calibration_pattern[:,:2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

# Create arrays to store object points and image points from all the images
object_points = []
image_points = []

# Load the images and detect the calibration pattern
for i in range(5565, 5579):
    # Load the image
    img = cv2.imread('calibration_images/IMG_{}.jpg'.format(i))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the calibration pattern corners
    found, corners = cv2.findChessboardCorners(gray, pattern_size, None)

    # If the pattern is found, add object points and image points
    if found:
        object_points.append(calibration_pattern)
        image_points.append(corners)

# Calibrate the camera
retval, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, gray.shape[::-1], None, None)

# Print the camera matrix
print('Camera matrix:')
print(camera_matrix)
