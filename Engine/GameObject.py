from abc import ABC

from Engine import Game
from Engine.Camera import Camera
from Engine.Transform import Transform


class GameObject(ABC) :
    def __init__(self,name="",tags=["gameObjects"]):
        self.tags = tags
        self.name = name
        self.transform = Transform()
        self.Components = []
        self.destroy = False
        self.tracked = False
        self.Used = False


    def start(self):
        for c in self.Components :
            c.start()
        self.Used = True



    def update(self,dt):

        if self.tracked :
            Camera.DX = self.transform.position.x - Game.Game.game.width/2
            Camera.DY = self.transform.position.y - Game.Game.game.height/2

        if(not self.destroy) :
            for composant in self.Components:
                composant.update(dt)
                if(self.destroy) :
                    break
        else :
            Game.Game.game.CurrentScene.removeGameObject(self)


    def addComponent(self, composant):
        if self.Used :
            composant.start()
        self.Components.append(composant)



    def AttachCamera(self,state):
        self.tracked = state


    def getComponent(self,class_) :
        for el in self.Components :
            if el.__class__ == class_ :
                return el
        return None

    def end(self):
        pass