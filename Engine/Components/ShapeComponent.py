import Engine.Game as Window
import pygame as pg

from Engine.Camera import Camera
from Engine.Component import Component
from Engine.Transform import Transform


class ShapeComponent(Component) :
    def __init__(self,parent,color , shape=" ") :
        super().__init__(parent)
        if shape == " " or shape == "rect":
            self.shape = "rect"
        self.parent = parent

        self.transform = parent.transform
        self.color = color

    def start(self):
        pass

    def update(self,dt) :

        pg.draw.rect(Window.Game.game.surface, self.color,((
                                                 int(self.transform.position.x - Camera.DX),
                                                 int(self.transform.position.y ) - Camera.DY),
                                                 (int(self.transform.scale.x * Camera.ZX),
                                                  int(self.transform.scale.y * Camera.ZY))))

    def getSprite(self) :
        return self.sprite

    def setSprite(self, sprite) :
        self.sprite = sprite