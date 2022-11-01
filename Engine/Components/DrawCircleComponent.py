import Engine.PyGineGame as Game
import pygame as pg

from Engine.Camera import Camera
from Engine.Component import Component
from Engine.Transform import Transform


class DrawCircleComponent(Component) :
    def __init__(self,parent,color,InitialRadius=1 ) :
        super().__init__(parent)



        self.parent = parent

        self.transform = Transform()
        self.transform.scale.x = InitialRadius


        self.color = color

    def start(self):
        pass

    def update(self,dt) :

        pg.draw.circle(Game.get().surface,self.color,(int((self.parent.transform.position.x + self.transform.position.x) - Camera.DX),
                         int((self.parent.transform.position.y +self.transform.position.y) - Camera.DY) ) , self.transform.scale.x*Camera.ZX)


    def getSprite(self) :
        return self.sprite

    def setSprite(self, sprite) :
        self.sprite = sprite