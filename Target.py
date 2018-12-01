import numpy as np
import cv2
from TargetDetector import TargetDetector

class Target:
	def __init__(self):
		self.maxX = 0
		self.maxY = 0
		self.minX = 1000
		self.minY = 1000
		self.width = 0
		self.height = 0
		self.centerX = 0
		self.centerY = 0
		self.shape = "Nothing"
	def getWidth(self, approx):
		for i in approx:
			if (i[0][0] > self.maxX):
				self.maxX = i[0][0]
			if (i[0][0] < self.minX):
				self.minX = i[0][0]
		self.width = self.maxX - self.minX
		return self.width
	def getHeight(self, approx):
		for i in approx:
			if (i[0][1] > self.maxY):
				self.maxY = i[0][1]
			if (i[0][1] < self.minY):
				self.minY = i[0][1]
		self.height = self.maxY - self.minY
		return self.height
	def getCenter(self):
		self.centerX = (self.maxX + self.minX)/2
		self.centerY = (self.maxY + self.minY)/2
		return self.centerX, self.centerY
	def getShape(self, targetApprox):
		if (len(targetApprox) == 4):
			self.shape = "Rectangle"
		if (len(targetApprox) == 12):
			self.shape = "Plus"
		return self.shape
			