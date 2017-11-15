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
			self.coords[1] -= self.speed
		elif direction == "down":
			self.coords[1] += self.speed
		elif direction == "right":
			self.coords[0] += self.speed
		elif direction == "left":
			self.coords[0] -= self.speed

	def draw(self, window, trail):
		pygame.draw.rect(window, self.color, (self.coords, self.size))
		for coord in trail:
			pygame.draw.rect(window, self.color, (coord, self.size))

	def check_boundaries(self, screen_size):
		for i in [0, 1]:
			if self.coords[i] < 0:
				self.coords[i] = 0
			elif self.coords[i] > screen_size[i] - self.size[i]:
				self.coords[i] = screen_size[i] - self.size[i]

	def has_collided(self, player, trailplayer1, trailplayer2):
		collided = False
		for coord1 in trailplayer2:
			for coord2 in trailplayer1:
				if ((coord1[0] < coord2[0] + player.size[0]) and
			(coord2[0] < coord1[0] + self.size[0]) and
			(coord1[1] < coord2[1] + player.size[1]) and
			(coord2[1] < coord1[1] + self.size[1])):
					collided = True
		return collided

	def reset(self):
		window.fill(pygame.Color('white'))
		self.coords = list(self.initial_coords)

WINDOW_SIZE = [100, 100]
PLAYER_SIZE = [10, 10]
player1 = Player(
	pygame.Color("red"), 
	[0, 0],
	PLAYER_SIZE, 
	1
)
player2 = Player(
	pygame.Color("blue"),
	[WINDOW_SIZE[0] - PLAYER_SIZE[0], WINDOW_SIZE[1] - PLAYER_SIZE[1]],
	PLAYER_SIZE,
	1
)
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
trailplayer1 = []
trailplayer2 = []
window.fill(pygame.Color('white'))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		keys = pygame.key.get_pressed()
		pygame.draw.rect(window, player1.color, (player1.coords, player1.size))
		pygame.draw.rect(window, player2.color, (player2.coords, player2.size))
		if keys[pygame.K_RIGHT]:
			player1.move('right')
		elif keys[pygame.K_LEFT]:
			player1.move('left')
		if keys[pygame.K_UP]:
			player1.move('up')
		elif keys[pygame.K_DOWN]:
			player1.move('down')
		trailplayer1.append(player1.coords)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			player2.move('right')
		elif keys[pygame.K_a]:
			player2.move('left')
		if keys[pygame.K_w]:
			player2.move('up')
		elif keys[pygame.K_s]:
			player2.move('down')
		trailplayer2.append(player2.coords)


	player1.check_boundaries(WINDOW_SIZE)
	player2.check_boundaries(WINDOW_SIZE)

	if player1.has_collided(player2, trailplayer1, trailplayer2) or player2.has_collided(player1, trailplayer1, trailplayer2):
		player1.reset()
		player2.reset()
		trailplayer1 = []
		trailplayer2 = []


	player1.draw(window, trailplayer1)
	player2.draw(window, trailplayer2)

	pygame.display.update()

	clock.tick(60)