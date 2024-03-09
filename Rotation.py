import cv2

path='C:/Users/zubai/Downloads/car.webp'
src=cv2.imread(path)
window="image"
image=cv2.rotate(src,cv2.ROTATE_180)
cv2.imshow(window,image)
cv2.waitKey(0)
