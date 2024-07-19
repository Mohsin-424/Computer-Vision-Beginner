import numpy as np
import cv2


def get_limits(color):
    """Calculates color limits in HSV for inRange based on BGR color."""

    c = np.uint8([[color]])  # Convert color to uint8 for OpenCV

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)  # Ensure consistent data type
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
