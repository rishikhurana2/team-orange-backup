import cv2
import numpy as np

class TargetDetector:
	def __init__(self):
		self.threshed = None
		self.contr = None
		self.HSV = None
		self.origImg = None
		self.targetApprox = np.zeros((0,0,0))
		self.approx = None
		self.maxX = 0
		self.minX = 1000
		self.maxY = 0
		self.minY = 1000
		self.maxXReturn = 0
		self.minXReturn = 1000
		self.maxYReturn = 0
		self.minYReturn = 1000
	def threshold(self, originalImage):
		self.origImg = originalImage
		self.HSV = cv2.cvtColor(self.origImg, cv2.COLOR_BGR2HSV)
		THRESHOLD_MIN = np.array([30,0,200], np.uint8)
		THRESHOLD_MAX = np.array([90,255,255], np.uint8)
		self.threshed = cv2.inRange(self.HSV, THRESHOLD_MIN, THRESHOLD_MAX)
	def contour(self):
		count = -1
		images, contours, hierarchy = cv2.findContours(self.threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for cont in contours:
			count = count + 1
			self.approx = cv2.approxPolyDP(cont, 0.1 * cv2.arcLength(cont, True), True)
			area = cv2.contourArea(self.approx)
			if (len(self.approx) >= 4 and area > 1000):
				self.targetApprox = self.approx
				cv2.drawContours(self.origImg, contours, count, (255,10,255), 5)
				self.maxX = 0
				self.minX = 1000
				self.maxY = 0
				self.minY = 1000
				for i in self.approx:
					if (i[0][0] > self.maxX):
						self.maxX = i[0][0]
					if (i[0][0] < self.minX):
						self.minX = i[0][0]
					if (i[0][1] > self.maxY):
						self.maxY = i[0][1]
					if (i[0][1] < self.minY):
						self.minY = i[0][1]
				self.maxXReturn = self.maxX
				self.maxYReturn = self.maxY
				self.minXReturn = self.minX
				self.minYReturn = self.minY
		self.contr = self.origImg
	def getTargetApprox(self):
		return self.targetApprox
	def getApprox(self):
		return self.approx
	def getExtrema(self):
		return self.maxXReturn, self.minXReturn, self.maxYReturn, self.minYReturn
	def getContour(self):
		return self.contr
	def getHSV(self):
		return self.HSV
	def getThreshed(self):
		return self.threshed