from Engine import Debug, PyGineGame as Game
from Engine.Scene import Scene
from GameWorkspace.GameObjects.MonsterManager import MonsterManager

from GameWorkspace.Scripts.MonsterManagerScript import MonsterManagerScript
from GameWorkspace.Scripts.playerScript import PlayerScript


class SecondScene(Scene) :
    def __init__(self):
        super().__init__()
        self.monstermanager = MonsterManager(5000)

    def earlyStart(self):
        Game.get().instanciate(Game.get().player)
        Game.get().instanciate(self.monstermanager)


    def start(self):


        Debug.PrintDebug("StartScene start " + str(len(self.GameObjects)) + " game objects")

    def update(self,dt):
        Game.get().surface.fill((0,100,255))

