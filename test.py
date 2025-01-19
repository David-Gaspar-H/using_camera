import cv2
import numpy as np

def camera():
	cap = cv2.VideoCapture(1)

	if not cap.isOpened():
		print("Cam not detected")
		return
  
	while True:
		ret, frame = cap.read()

		if not ret:
			print("Not capturing frames")
			return
		height, width = frame.shape[:2]
		print(height, width)

		cv2.imshow('Cam feed', frame)

		if cv2.waitKey(1) == ord('q'):
			break
	
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	camera()