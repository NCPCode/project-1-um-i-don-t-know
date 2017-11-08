import pygame
from turtle import *

class Player:
	def __init__(self, color, coords, size, speed, playerTurtle):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.size = size
		self.speed = speed
		self.playerTurtle = playerTurtle

	def move(self, direction):
		if direction == "up":
			self.coords[1] -= speed
		elif direction == "down":
			self.coords[1] += speed
		elif direction == "right":
			self.coords[0] += speed
		elif direction == "left":
			self.coords[0] -= speed

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self,coords, self.size))

	def check_boundaries(self, screen_size):
    	for i in [0, 1]:
      		if self.coords[i] < 0:
        		self.coords[i] = 0
      		elif self.coords[i] > screen_size[i] - self.size[i]
        		self.coords[i] = screen_size[i] - self.size[i]

    def has_collided(self, player):
    	return ((self.coords[0] < player.coords[0] + player.size[0]) and
            (player.coords[0] < self.coords[0] + self.size[0]) and
            (self.coords[1] < player.coords[1] + player.size[1]) and
            (player.coords[1] < self.coords[1] + self.size[1]))

    def reset(self):
    	self.coords = list(self.initial_coords)