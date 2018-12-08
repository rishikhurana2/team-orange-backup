import numpy as np

class TargetProcessor:
	def __init__(self):	
		self.alti = 0
		self.azi = 0
		self.dist = 0
		self.realRectWidth = 12.7
		self.realPlusWidth = 6.5
		self.focalLength = 700
	def calculate(self, width, height, centerX, centerY, frame, shape):
		xOffset = frame.shape[0]/2 - centerX
		yOffset = frame.shape[1]/2 - centerY		
		if (shape == "Rectangle"):
			self.dist = (self.focalLength * self.realRectWidth)/width
		if (shape == "Cross"):
			self.dist = (self.focalLength * self.realPlusWidth)/width
		self.azi = np.arctan(xOffset/self.focalLength) * 180/np.pi
		self.alti = np.arctan(yOffset/self.focalLength) * 180/np.pi
	def getAzi(self):
		return self.azi
	def getAlti(self):
		return self.alti
	def getDist(self):
		return self.dist