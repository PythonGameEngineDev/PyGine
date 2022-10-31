import Engine.Game as Window
import pygame as pg

from Engine.Camera import Camera
from Engine.Component import Component
from Engine.Transform import Transform


class DrawCircleComponent(Component) :
    def __init__(self,parent,color ) :
        super().__init__(parent)

        self.parent = parent

        self.transform = parent.transform
        self.color = color

    def start(self):
        pass

    def update(self,dt) :

        pg.draw.circle(Window.Game.game.surface,self.color,(int(self.transform.position.x - Camera.DX),
                         int(self.transform.position.y - Camera.DY) ) , self.transform.scale.x*Camera.ZX)


    def getSprite(self) :
        return self.sprite

    def setSprite(self, sprite) :
        self.sprite = sprite