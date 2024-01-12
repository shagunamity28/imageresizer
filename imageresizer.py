import cv2

image  = cv2.imread("radha.png" , cv2.IMREAD_UNCHANGED)
cv2.imshow("title" , image )
#percent by which image is resized 
scale_percent = 50

#calculate the 80 percent of the original dimesnions 
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int (image.shape[0]  * scale_percent / 100)

#resizing 
output = cv2.resize(image, (new_width,new_width))


cv2.imwrite( 'new_image.png' , output)
cv2.waitKey(0)