from Engine import Debug
from Engine.Scene import Scene
import Engine.PyGineGame as Game
from Engine.Vector3 import Vector3
from GameWorkspace.GameObjects.Barrier import Barrier
from GameWorkspace.GameObjects.MonsterManager import MonsterManager
from GameWorkspace.GameObjects.Player import Player
from GameWorkspace.GameObjects.Monster import Monster
from GameWorkspace.Scripts import playerScript
from GameWorkspace.Scripts.MonsterManagerScript import MonsterManagerScript
from GameWorkspace.Scripts.playerScript import PlayerScript



class StartScene(Scene):
    def __init__(self):
        super().__init__()
        self.monstermanager = MonsterManager(1000)

    def earlyStart(self):
        Game.get().instanciate(Game.get().player)
        Game.get().instanciate(self.monstermanager)



    def start(self):

        Debug.PrintDebug("je passe apres pour set le nb")
        Debug.PrintDebug("StartScene start " + str(len(self.GameObjects)) + " game objects")

    def update(self,dt):
        Game.get().surface.fill((255,100,0))


        if(Game.get().player.getComponent(PlayerScript).points >=self.monstermanager.nbmonsters) :
            Game.get().setScene(1)
