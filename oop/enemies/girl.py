import pygame
from oop.enemy import Enemy

class Girl(Enemy):
  
  speed = 5
  
  def setup(self):
    self.speed = Girl.speed
  
  def tiles(self):
    return [
      pygame.image.load('resources/images/girl.png'),
      pygame.image.load('resources/images/girl.png'),
      pygame.image.load('resources/images/girl.png'),
      pygame.image.load('resources/images/girl.png')
    ]
  
  def hit_sound(self):
    tmp = pygame.mixer.Sound("resources/audio/enemy.wav")
    tmp.set_volume(0.05)
    tmp.play()