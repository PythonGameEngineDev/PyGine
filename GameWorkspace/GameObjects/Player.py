from Engine import Debug
from Engine.Components.BoxComponent import BoxComponent
from Engine.Components.ShapeComponent import ShapeComponent
from Engine.Components.TextComponent import TextComponent
from GameWorkspace.Scripts import playerScript
from Engine.GameObject import GameObject


class Player(GameObject) :
    def __init__(self):
        super().__init__("Player")


    def start(self):
        Debug.PrintDebug("player start")
        self.addComponent(ShapeComponent(self,(255,255,255)))
        self.addComponent(playerScript.PlayerScript(self))
        self.addComponent(BoxComponent(self))
        self.addComponent(TextComponent(self,"None"))

        super().start()

    def update(self,dt):
        super().update(dt)

    def end(self):
        Debug.PrintDebug("player end")