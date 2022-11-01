from Engine import Debug
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.GameObject import GameObject
from GameWorkspace.Scripts.MonsterScript import MonsterScript


class Monster(GameObject):

    def start(self):
        Debug.PrintDebug("Monster start")
        self.addComponent(DrawRectComponent(self,(255,0,0)))
        self.addComponent(MonsterScript(self))
        self.addComponent(BoxColliderComponent(self))