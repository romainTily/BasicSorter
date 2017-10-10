import sys
import os
import pygame
import random
import math
from pygame.locals import *

class BASIC():
	def __init__(self):
		self.indSample = []

		self.initCONST()
		self.firstRun()

		self.firstSorter()



	def ghettoLog(self,data):
		with open("log.txt","a+") as f:
			f.write(str(data)+"\n")


	def initCONST(self):
		self.HEIGHT = 640
		self.WIDTH = 1300

		self.SAMPLE_NUMBER = 6

		self.baseWidth = math.floor(self.WIDTH/((self.SAMPLE_NUMBER*2)+1))

		self.color = {'white' : (255,255,255),
					  'light blue' : (25,201,255),
					  'grey' : (60,60,60),
					  'black' : (0,0,0)}


	def drawCursor(self,ind):
		ecart = self.baseWidth*(ind*2)

		#cursor
		pygame.draw.polygon(self.dsp, self.color["white"], [ [ecart+(self.baseWidth*1.5),620], 
															 [ecart+(self.baseWidth*1.4),630], 
															 [ecart+(self.baseWidth*1.6),630]])
		
		#+ cursor outline (no outline)
		# pygame.draw.polygon(self.dsp,self.color["light blue"],[[ind*(baseWidth*1.5),620],[ind*baseWidth,630],[ind*(baseWidth*2),630]],1)


	def drawSamples(self, heightList, selected=[]):
		startY = self.HEIGHT-40 ; ecart = 0

		for i, height in enumerate(heightList):
			ecart += self.baseWidth

			color = self.color['grey'] if i in selected else self.color['black']

			self.drawOne(i,self.baseWidth,ecart,height,startY,color)


	def drawOne(self, n, width, ecart, height,startY,color):
		pygame.draw.rect(self.dsp, color, ((width*n)+ecart, startY, width, -height))

		#the outline fuck my adaptative layout, gush
		# pygame.draw.rect(self.dsp, self.color['grey'],(width*n+ecart, startY, width, -height), 3)


	def firstRun(self):
		pygame.init()

		self.dsp = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
		self.dsp.fill(self.color["white"])

		#rect at the bottom
		pygame.draw.rect(self.dsp,self.color["black"],(0,self.HEIGHT,self.WIDTH,-39))

		#cursor at ind 0
		self.drawCursor(0)

		#first random render, rect are randomly ordered (some value are hard coded)
		firstRandom = [i for i in range(math.floor(300/self.SAMPLE_NUMBER*2), self.HEIGHT, math.floor(300/self.SAMPLE_NUMBER*2))]
		random.shuffle(firstRandom)

		#then draw them
		self.drawSamples(firstRandom)

		#store them in the ind list
		self.indSample.extend(firstRandom)

		self.ghettoLog(self.indSample)


	def nextFrame(self):
		self.dsp.fill(self.color["white"])



		#redraw the rect
		pygame.draw.rect(self.dsp,self.color["black"],(0,self.HEIGHT,self.WIDTH,-39))




	def firstSorter(self):
		while True:

			self.nextFrame()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()




basic_app = BASIC()
print(test)