import cv2
import numpy as np

image = np.full((400, 600, 3), 255, dtype=np.uint8)

cv2.rectangle(image, (60, 80), (260, 300), (255, 0, 0), 4)
cv2.circle(image, (430, 190), 90, (0, 0, 255), 4)
cv2.putText(image, "OpenCV", (210, 360), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 128, 0), 3)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 160)

cv2.imwrite("opencv-original.png", image)
cv2.imwrite("opencv-gray.png", gray)
cv2.imwrite("opencv-edges.png", edges)

print("OpenCV image processing finished.")
print("Created: opencv-original.png, opencv-gray.png, opencv-edges.png")
