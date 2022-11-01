from Engine import Debug
from Engine.Scene import Scene
import Engine.PyGineGame as Game
from GameWorkspace.GameObjects.Player import Player
from GameWorkspace.GameObjects.Monster import Monster

class StartScene(Scene):
    def __init__(self):
        super().__init__()
        self.player = Player()


    def start(self):

        self.addGameObject(self.player)

        for i in range(10000) :
            Game.get().instanciate(Monster())
            #self.addGameObject(Monster())
        Debug.PrintDebug("StartScene start " + str(len(self.GameObjects)) + " game objects")

    def update(self,dt):
        Game.get().surface.fill((255,100,0))

