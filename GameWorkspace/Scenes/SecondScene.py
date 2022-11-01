from Engine import Debug
from Engine.Scene import Scene
import Engine.Game as Window
from GameWorkspace.GameObjects.Monster import Monster
from GameWorkspace.GameObjects.Player import Player


class SecondScene(Scene) :
    def start(self):
        for i in range(1) :
            self.addGameObject(Player())


        super().start()
        Debug.PrintDebug("SecondScene start " + str(len(self.GameObjects)) + " game objects")

    def update(self,dt):

        Window.Game.game.surface.fill((0,100,110))
        super().update(dt)
