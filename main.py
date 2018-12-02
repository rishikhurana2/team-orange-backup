from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from Target import Target
import cv2

cameraID = 1

cam = cv2.VideoCapture(cameraID)
detector = TargetDetector()
target = Target()
processor = TargetProcessor()

plusCount = 0
rectCount = 0

while(True):
	ret,frame = cam.read()
	if not ret:
		continue
	detector.threshold(frame)
	detector.contour()
	targetApprox = detector.getTargetApprox()
	#approx = detector.getApprox()
	print(targetApprox)
	maxX, minX = detector.getXExtrema()
	maxY, minY = detector.getYExtrema()
	width = target.getWidth(minX, maxX)
	height = target.getHeight(minY, maxY)
	print(maxX)
	print(minX)
	print(width)
	print(height)
	centerX, centerY = target.getCenter()
	shape = target.getShape(targetApprox)
	processor.calculate(width, height, centerX, centerY, detector.getHSV(), shape)
	azi = processor.getAzi()
	#alti = processor.getAlti()
	dist = processor.getDist()
	cv2.imshow("Threshed Image", detector.getThreshed())
	cv2.imshow("Contoured Image", detector.getContour())
	#print(shape)
	#print("Azimuth: " + str(azi))
	#print("Altitude: " + str(alti))
	#print("Distance: " + str(dist))
	if (cv2.waitKey(10) == 27):
		break