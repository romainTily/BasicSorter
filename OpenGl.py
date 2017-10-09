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

		self.drawHUD()
		self.drawSamples(self.SAMPLE_NUMBER)

		self.main_loop()



	def ghettoLog(self,data):
		with open("log","a+") as f:
			f.write(data+"\n")


	def initCONST(self):
		self.HEIGHT = 640
		self.WIDTH = 1300

		self.SAMPLE_NUMBER = 10

		self.color = {'white' : (255,255,255),
					  'light blue' : (25,201,255),
					  'grey' : (60,60,60),
					  'black' : (0,0,0)}


	def initScreen(self):
		pygame.init()

		self.dsp = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
		self.dsp.fill(self.color["white"])


	# def select(self):


	def drawHUD(self):

		#line
		pygame.draw.line(self.dsp,self.color["black"],(0,600),(1300,600),3)

		baseWidth = self.WIDTH/(self.SAMPLE_NUMBER*2)

		#cursor
		cursor = pygame.draw.polygon(self.dsp,self.color["black"],[[baseWidth*1.5,620],[baseWidth,640],[baseWidth*2,640]],2)
		
		#+ cursor outline
		#pygame.draw.polygon(self.dsp,self.color["light blue"],[[baseWidth*1.5,620],[baseWidth,640],[baseWidth*2,640]],4)


	def moveCursor(n):
		pass

	def inverteSample(self,n1,n2):
		#fill white
		#draw new
		#fill white
		#draw new

		pass


	def drawSamples(self,n):
		width = self.WIDTH/(n*2)
		height = [i for i in range(math.floor(300/n*2),self.HEIGHT-40,math.floor(300/n*2))]
		startY = self.HEIGHT-40 ; ecart = 0

		random.shuffle(height)


		for i, height in enumerate(height):
			ecart += width
			self.drawSample(i,width,ecart,height,startY)

	def drawSample(self, n, width, ecart, height,startY):
		pygame.draw.rect(self.dsp, self.color['black'],(width*n+ecart, startY, width, -height))
		pygame.draw.rect(self.dsp, self.color['grey'],(width*n+ecart, startY, width, -height), 3)



	def main_loop(self):
		while True:

			#pygame.draw.rect(self.dsp,self.color['black'],(0,0,10,10))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()

basic_app = BASIC()
print(test)