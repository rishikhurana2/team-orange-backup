from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from Target import Target
import cv2

cameraID = 1

cam = cv2.VideoCapture(cameraID)
detector = TargetDetector()
target = Target()
processor = TargetProcessor()

while(True):
	ret,frame = cam.read()
	if not ret:
		continue
	detector.threshold(frame)
	detector.contour()
	maxX, minX, maxY, minY = detector.getExtrema()
	targetApprox = detector.getTargetApprox()
	width = target.getWidth(maxX, minX)
	height = target.getHeight(maxY, minY)
	centerX, centerY = target.getCenter()
	shape = target.getShape(targetApprox)
	processor.calculate(width, height, centerX, centerY, frame, shape)
	azi = processor.getAzi()
	cv2.imshow("Threshed Image", detector.getThreshed())
	cv2.imshow("Contoured Image", detector.getContour())
	
	print("Azimuth: " + str(azi))
	if (cv2.waitKey(10) == 27):
		break