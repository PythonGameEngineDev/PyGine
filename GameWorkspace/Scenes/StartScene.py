from Engine import Debug
from Engine.Scene import Scene
import Engine.Game as Window
from GameWorkspace.GameObjects.Player import Player
from GameWorkspace.GameObjects.Monster import Monster

class StartScene(Scene):
    def __init__(self):
        super().__init__("StartScene")
        self.player = Player()


    def start(self):

        self.addGameObject(self.player)

        for i in range(1) :
            self.addGameObject(Monster())

        super().start()
        Debug.PrintDebug("StartScene start " + str(len(self.GameObjects)) + " game objects")

    def update(self,dt):
        Window.Game.game.surface.fill((255,100,0))
        super().update(dt)

