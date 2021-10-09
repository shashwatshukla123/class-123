import numpy as np
import cv2

#numpy.ones reshapes the array--width600,height 800
rect=np.ones((600,800,3),dtype=np.uint8)*255

#bgr--red color below one
#10 is the thickness
cv2.rectangle(rect,(0,int(600/2)),(int(800/2),599),(0,0,255),10)
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()

#bgr below in green
#-1 so no border
cv2.rectangle(rect,(int(800/2),0),(799,int(600/2)),(0,255,0),9)
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()

#image: It is the image on which rectangle is to be drawn.
#start_point: It is the starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
#end_point: It is the ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
#color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
#thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.
#Return Value: It returns an image.