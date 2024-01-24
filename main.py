import cv2

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Original image of python", image)
scale = 50

new_width = int(image.shape[1] * scale/100)
new_height = int(image.shape[0] * scale/100)

output = cv2.resize(image, (new_width, new_height))
cv2.imshow("resized image", output)
cv2.waitKey(0)
