import numpy as np
import cv2
from TargetDetector import TargetDetector

class Target:
	def __init__(self):
		self.maxX = 0
		self.maxY = 0
		self.minX = 0
		self.minY = 0
		self.width = 0
		self.height = 0
		self.centerX = 0
		self.centerY = 0
		self.shape = "Nothing"
		self.detector = TargetDetector()
	def getWidth(self, maxX, minX): 
		self.minX = minX
		self.maxX = maxX
		self.width = self.maxX - self.minX
		return self.width
	def getHeight(self, maxY, minY):
		self.minY = minY
		self.maxY = maxY
		self.height = self.maxY - self.minY
		return self.height
	def getCenter(self):
		self.centerX = (self.maxX + self.minX)/2
		self.centerY = (self.maxY + self.minY)/2
		return self.centerX, self.centerY
	def getShape(self, targetApprox):
		if (len(targetApprox) > 0):
			if (len(targetApprox) == 4):
				self.shape = "Rectangle"
			if (len(targetApprox) == 12):
				self.shape = "Cross"
		return self.shape
			