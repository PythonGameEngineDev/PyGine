import random
import GameWorkspace
from Engine import Game, Debug, KeyListener
from Engine.Camera import Camera
from Engine.Component import Component
from Engine.Components.TextComponent import TextComponent
from Engine.Vector3 import Vector3
import pygame as pg

class PlayerScript(Component) :
    def __init__(self, parent):
        super().__init__(parent)
        self.speed = 0.5
        self.points = 0

    def start(self):
        self.parent.transform.position = Vector3(0,0, 0)
        self.parent.transform.scale = Vector3(100,100,100)
        self.parent.AttachCamera(True)
        Debug.PrintDebug("PlayerScript start")

    def update(self, dt):

        self.parent.transform.position.y -= self.speed*dt * KeyListener.getPressed(pg.K_z)
        self.parent.transform.position.y += self.speed*dt * KeyListener.getPressed(pg.K_s)

        self.parent.transform.position.x -= self.speed*dt * KeyListener.getPressed(pg.K_q)
        self.parent.transform.position.x += self.speed*dt * KeyListener.getPressed(pg.K_d)

        self.parent.getComponent(TextComponent).setText(str(self.points))


        """
        if self.parent.transform.position.x > 1000 or self.parent.transform.position.y > 600 :
            self.parent.destroy = True
            Window.Game.game.CurrentScene.addGameObject(GameWorkspace.GameObjects.Player.Player())
        """