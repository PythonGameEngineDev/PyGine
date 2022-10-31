from Engine import Debug
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.GameObject import GameObject
from GameWorkspace.Scripts.MonsterScript import MonsterScript


class Monster(GameObject):
    def __init__(self):
        super().__init__("Monster")

    def start(self):

        Debug.PrintDebug("Monster start")
        self.addComponent(DrawRectComponent(self,(255,0,0)))
        self.addComponent(MonsterScript(self))
        self.addComponent(BoxColliderComponent(self))
        super().start()

    def update(self,dt):
        super().update(dt)

    def end(self):
        Debug.PrintDebug("Monster end")
