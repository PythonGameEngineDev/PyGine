import random

from Engine import Debug
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.GameObject import GameObject
from Engine.Vector3 import Vector3
from GameWorkspace.Scripts.MonsterManagerScript import MonsterManagerScript


class MonsterManager(GameObject):
    def __init__(self,nbMonsters):
        super().__init__()
        self.nbmonsters = nbMonsters
    def start(self):

        self.addComponent(MonsterManagerScript(self,self.nbmonsters))
