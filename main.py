import pygame
from oop.bullets.Love import Love
from oop.bullets.Peluru import Peluru
from oop.control import GameController
from oop.scene import Scene
from oop.levels.level1 import Level1
from oop.levels.level2 import Level2
from oop.levels.level3 import Level3
from oop.levels.level4 import Level4
from oop.levels.level5 import Level5
from oop.player import Player

pygame.init()

scene = Scene((640, 480))
scene.setup_level(
  Level1,
  Level2,
  Level3,
  Level4,
  Level5,
)
#===============================#
#Pilih Map Sesuai Anda Inginkan
# 1.Default
# 2.Padang Pasir
# 3.Dalam Laut
# 4.Galaxy
# 5.Kota
scene.next_level()
#scene.next_level()
#scene.next_level()
#scene.next_level()
#===============================#
#Pilih Senjata Yang Anda Suka
# 1.Mine
# 2.Bomb
player = Player(scene,Love())
#player = Player(scene, Peluru())
game_controller = GameController(player)

running = True

while(running):
  scene.fill()
  game_controller.keyboard_event()
  game_controller.mouse_position_event()
  pygame.display.flip()