import random

from Engine import Debug
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.GameObject import GameObject
from Engine.Vector3 import Vector3
from GameWorkspace.Scripts.MonsterScript import MonsterScript


class Monster(GameObject):



    def start(self):
        Debug.PrintDebug("Monster start")


        self.addComponent(DrawRectComponent(self,(255,0,0)))

        self.addComponent(BoxColliderComponent(self))

        self.addComponent(MonsterScript(self))
