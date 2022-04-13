import pygame
from oop.enemies.scorpion import Scorpion
from oop.level import Level
from oop.levels.castle.castle1 import Castle
from oop.enemies.mouse import Mouse


class Level4(Level):
    ''' Level 4 - berlatar belakang galaxy '''

    def setup(self):
        self.castle = Castle(self.screen)
        self.enemy = [Mouse, Scorpion]

    def background_sound(self, volume=0.25):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/audio/milkiway.mp3")
        pygame.mixer.music.play(-4, 0.0)
        pygame.mixer.music.set_volume(volume)

    def tiles(self):
        return pygame.image.load('resources/images/bglove.jpg')
        
