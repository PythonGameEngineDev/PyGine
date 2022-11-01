import random
from Engine import PyGineGame as Game, Debug
from Engine.Component import Component
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.CircleColliderComponent import CircleColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.Vector3 import Vector3
from GameWorkspace.GameObjects.Barrier import Barrier
from GameWorkspace.GameObjects.Monster import Monster
from GameWorkspace.Scripts.playerScript import PlayerScript


class MonsterManagerScript(Component):
    def __init__(self, parent,nbMonsters):
        super().__init__(parent)
        self.DX = 1000
        self.DY = 500
        self.X = -1000
        self.Y = -500
        self.NBmonsters = nbMonsters
        Debug.PrintDebug("je passe que maintenant ")

    def start(self):

        for i in range(self.NBmonsters):

            monster = Monster()
            monster.transform.position = Vector3(random.Random().randint(self.X, self.DX), random.Random().randint(self.Y, self.DY),
                                              0)
            monster.transform.scale = Vector3(10, 10, 10)
            Game.get().instanciate(monster)

        bar1 = Barrier()
        bar1.transform.scale = Vector3(Game.get().width,10,0)
        bar1.transform.position = Vector3(0,0,0)
        Game.get().instanciate(bar1)

    def update(self, dt):
        pass