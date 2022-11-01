from Engine.PyGineGame import Game
from GameWorkspace.Scenes.SecondScene import SecondScene
from GameWorkspace.Scenes.StartScene import StartScene
import pygame as pg


class MyFirstGame(Game) :
    def __init__(self):
        super().__init__(1000,600,self)

        self.addScene(StartScene())
        self.setScene(0)
        self.addScene(SecondScene())

    def update(self):
        pg.display.set_caption(str(self.game.dt))
        super().update()



MyFirstGame().run()