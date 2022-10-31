import random
from Engine import Game, Debug
from Engine.Components.BoxComponent import BoxComponent
from Engine.Component import Component
from Engine.Components.ShapeComponent import ShapeComponent
from Engine.Vector3 import Vector3
from GameWorkspace.Scripts.playerScript import PlayerScript


class MonsterScript(Component) :
    def __init__(self, parent):
        super().__init__(parent)
        self.R = 255

    def start(self):
        self.parent.transform.position = Vector3(random.Random().randint(-1000, 1000), random.Random().randint(-500, 500), 0)
        self.parent.transform.scale = Vector3(100,100,10)
        Debug.PrintDebug("monsterScript start")

    def update(self,dt):
        if(Game.Game.game.getCurrentScene().player.getComponent(BoxComponent).collide(self.parent.getComponent(BoxComponent))) :


            self.R = min(self.R+dt*1.2,255)

            self.parent.getComponent(ShapeComponent).color = (self.R,0,0)
            if self.R > 254 :
                self.parent.destroy = True
                Game.Game.game.getCurrentScene().player.getComponent(PlayerScript).points+=1

        else :

            self.R = max(self.R-dt*0.8,0)

            self.parent.getComponent(ShapeComponent).color = (self.R, 0, 0)