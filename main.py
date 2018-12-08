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
	#approx = detector.getApprox()
	maxX, minX, maxY, minY = detector.getExtrema()
	targetApprox = detector.getTargetApprox()
	width = target.getWidth(maxX, minX)
	height = target.getHeight(maxY, minY)
	#print(targetApprox)
	#print(str(width) + "_" + str(height))
	centerX, centerY = target.getCenter()
	shape = target.getShape(targetApprox)
	processor.calculate(width, height, centerX, centerY, frame, shape)
	azi = processor.getAzi()
	#alti = processor.getAlti()
	dist = processor.getDist()
	cv2.imshow("Threshed Image", detector.getThreshed())
	cv2.imshow("Contoured Image", detector.getContour())
	#print(shape)
	print("Azimuth: " + str(azi))
	#print("Altitude: " + str(alti))
	#print("Distance: " + str(dist))
	if (cv2.waitKey(10) == 27):
		break