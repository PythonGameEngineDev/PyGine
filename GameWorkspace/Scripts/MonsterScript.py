import random
from Engine import PyGineGame, Debug
from Engine.Component import Component
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.CircleColliderComponent import CircleColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.Vector3 import Vector3
from GameWorkspace.Scripts.playerScript import PlayerScript


class MonsterScript(Component) :
    def __init__(self, parent):
        super().__init__(parent)
        self.R = 255

    def start(self):
        self.parent.transform.position = Vector3(random.Random().randint(-1000, 1000), random.Random().randint(-500, 500), 0)
        self.parent.transform.scale = Vector3(10,10,10)
        Debug.PrintDebug("monsterScript start")

    def update(self,dt):
        if(PyGineGame.get().getCurrentScene().player.getComponent(CircleColliderComponent).collide(self.parent.getComponent(BoxColliderComponent))) :


            self.R = min(self.R+dt*1.2,255)

            self.parent.getComponent(DrawRectComponent).color = (self.R,0,0)
            if self.R > 254 :
                self.parent.destroy = True
                PyGineGame.get().getCurrentScene().player.getComponent(PlayerScript).points+=1

        else :

            self.R = max(self.R-dt*0.8,0)

            self.parent.getComponent(DrawRectComponent).color = (self.R, 0, 0)