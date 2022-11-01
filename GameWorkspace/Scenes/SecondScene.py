from Engine import Debug, PyGineGame
from Engine.Scene import Scene
import Engine.PyGineGame as Window
from GameWorkspace.GameObjects.Monster import Monster
from GameWorkspace.GameObjects.Player import Player


class SecondScene(Scene) :
    def start(self):
        for i in range(1) :
            PyGineGame.get().instanciate(Player())
        Debug.PrintDebug("SecondScene start " + str(len(self.GameObjects)) + " game objects")

    def update(self,dt):

        Window.Game.game.surface.fill((0,100,110))

