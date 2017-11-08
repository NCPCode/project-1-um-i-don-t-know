import pygame

class Player:
	def __init__(self, color, coords, size, speed):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.size = size
		self.speed = speed

	def move(self, direction):
		if direction == "up":
			self.coords[1] -= speed
		elif direction == "down":
			self.coords[1] += speed
		elif direction == "right":
			
