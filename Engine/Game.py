from abc import ABC

import pygame as pg

from Engine.Scene import Scene
from GameWorkspace.Scenes.StartScene import StartScene




class Game(ABC) :

    game = None
    def __init__(self, width, height,game) :
        Game.game = game
        pg.init()
        pg.event.set_allowed([pg.QUIT])
        self.width = width
        self.height = height
        self.surface = pg.Surface((width, height))
        self.FEN = pg.display.set_mode((width, height),  pg.DOUBLEBUF)
        self.running = True
        self.clock = pg.time.Clock()
        self.fps = 600
        self.dt = 0
        self.CurrentScene = None
        self.CurrentSceneID = -1
        self.scenes = []

    def run(self):
        while self.running:
            self.dt = self.clock.tick(self.fps)
            self.update()
            self.FEN.blit(self.surface, (0, 0))
            pg.display.flip()

    def update(self):
        for e in pg.event.get() :
            if e.type == pg.QUIT :
                exit()
        self.CurrentScene.update(self.dt)


    def setScene(self, ID):
        if self.CurrentScene :
            self.CurrentScene.end()
        self.CurrentSceneID = ID
        self.CurrentScene = self.scenes[ID]
        self.CurrentScene.start()


    def getSceneID(self):
        return self.CurrentSceneID

    def getCurrentScene(self)->Scene:
        return self.CurrentScene

    def addScene(self,scene):
        self.scenes.append(scene)

