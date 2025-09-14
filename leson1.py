import cv2
img=cv2.imread(r"images\pika.png",cv2.IMREAD_COLOR)
cv2.imshow("pika",img)

cv2.waitKey(0)

img3=cv2.imread(r"images\pika.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("pika black and white",img3)
cv2.waitKey(0)

img=cv2.imread(r"images\pika.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("pika unchangwd",img)
cv2.waitKey(0)
img2=cv2.imread(r"images\pika.png",cv2.IMREAD_COLOR)
b,g,r=cv2.split(img2)
cv2.imshow("pika red saturation",r)
cv2.imshow("pika blue saturation",b)
cv2.imshow("pika green saturation",g)
cv2.waitKey(0)
cv2.imwrite("modified.pmg",img3)