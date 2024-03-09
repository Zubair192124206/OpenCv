import cv2
import numpy as np
image = cv2.imread("C:/Users/zubai/OneDrive/Pictures/tom.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0, 0), 3)
high_boost_mask = gray - blur
boost_factor = 2
sharpened_image = gray + boost_factor * high_boost_mask
sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
