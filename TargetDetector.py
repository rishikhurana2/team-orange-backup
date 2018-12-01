import cv2
import numpy as np

class TargetDetector:
	def __init__(self):
		self.threshed = None
		self.approx = None
		self.contr = None
		self.HSV = None
		self.origImg = None
		self.targetApprox = None
		self.shape = "Nothing"
	def threshold(self, originalImage):
		self.origImg = originalImage
		self.HSV = cv2.cvtColor(self.origImg, cv2.COLOR_BGR2HSV)
		THRESHOLD_MIN = np.array([80,30,60], np.uint8)
		THRESHOLD_MAX = np.array([255,255,255], np.uint8)
		self.threshed = cv2.inRange(self.HSV, THRESHOLD_MIN, THRESHOLD_MAX)
	def contour(self):
		count = -1
		images, contours, hierarchy = cv2.findContours(self.threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for cont in contours:
			count = count + 1
			self.approx = cv2.approxPolyDP(cont, 0.03 * cv2.arcLength(cont, True), True)
			area = cv2.contourArea(self.approx)
			if (len(self.approx) >= 4 and area > 2000):
				self.targetApprox = self.approx
				cv2.drawContours(self.origImg, contours, count, (255,10,255), 5)
		self.contr = self.origImg
	def getTargetApprox(self):
		return self.targetApprox
	def getContour(self):
		return self.contr
	def getHSV(self):
		return self.HSV
	def getThreshed(self):
		return self.threshed
	def getShape(self):
		return self.shape 