import cv2
import numpy as np
img=cv2.imread('C:/Users/zubai/Downloads/tom.jpeg')
rows,cols,_=img.shape
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
m=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,m,(cols,rows))
cv2.imshow("Affine Transform",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

