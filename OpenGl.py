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
		self.initScreen()

		self.firstSorter()



	def ghettoLog(self,data):
		with open("log.txt","a+") as f:
			f.write(data+"\n")


	def initCONST(self):
		self.HEIGHT = 640
		self.WIDTH = 1300

		self.SAMPLE_NUMBER = 1

		self.color = {'white' : (255,255,255),
					  'light blue' : (25,201,255),
					  'grey' : (60,60,60),
					  'black' : (0,0,0)}


	def drawCursor(self,ind):
		ind+=1 ; 

		baseWidth = self.WIDTH/(self.SAMPLE_NUMBER*2)

		ecart = baseWidth*ind

		#cursor
		pygame.draw.polygon(self.dsp,self.color["white"],[[ecart+ind*(baseWidth*1.5),620],[ecart+ind*(baseWidth*1.2),630],[ecart+ind* (baseWidth*1.8) ,630]])
		
		#+ cursor outline (no outline)
		# pygame.draw.polygon(self.dsp,self.color["light blue"],[[ind*(baseWidth*1.5),620],[ind*baseWidth,630],[ind*(baseWidth*2),630]],1)


	def drawSamples(self,heightList):
		width = self.WIDTH/(self.SAMPLE_NUMBER*2)
		startY = self.HEIGHT-40 ; ecart = 0

		for i, height in enumerate(heightList):
			ecart += width
			self.drawOne(i,width,ecart,height,startY)


	def drawOne(self, n, width, ecart, height,startY):
		pygame.draw.rect(self.dsp, self.color['black'],(width*n+ecart, startY, width, -height))

		#the outline fuck my adaptative layout, gush
		# pygame.draw.rect(self.dsp, self.color['grey'],(width*n+ecart, startY, width, -height), 3)


	def initScreen(self):
		pygame.init()

		self.dsp = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
		self.dsp.fill(self.color["white"])

		#rect at the bottom
		pygame.draw.rect(self.dsp,self.color["black"],(0,self.HEIGHT,self.WIDTH,-39))

		#cursor at ind 0
		self.drawCursor(0)

		#first random render, rect are randomly ordered (some value are hard coded)
		firstRandom = [i for i in range(math.floor(300/self.SAMPLE_NUMBER*2), self.HEIGHT-40,math.floor(300/self.SAMPLE_NUMBER*2))]
		random.shuffle(firstRandom)

		#then draw them
		self.drawSamples(firstRandom)

		#store them in the ind list
		self.indSample.extend(firstRandom)


	def nextFrame():
		pass


	def firstSorter(self):
		while True:

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()




basic_app = BASIC()
print(test)