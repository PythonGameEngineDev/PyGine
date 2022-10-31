from Engine import Debug
from Engine.Components.BoxComponent import BoxComponent
from Engine.Components.ShapeComponent import ShapeComponent
from Engine.GameObject import GameObject
from GameWorkspace.Scripts.MonsterScript import MonsterScript


class Monster(GameObject) :
    def __init__(self):
        super().__init__("Monster")

    def start(self):

        Debug.PrintDebug("Monster start")
        self.addComponent(ShapeComponent(self,(255,0,0)))
        self.addComponent(MonsterScript(self))
        self.addComponent(BoxComponent(self))
        super().start()
    def update(self,dt):
        super().update(dt)

    def end(self):
        Debug.PrintDebug("Monster end")
