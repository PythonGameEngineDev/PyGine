from Engine import Debug
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.CircleColliderComponent import CircleColliderComponent
from Engine.Components.DrawCircleComponent import DrawCircleComponent
from Engine.Components.TextComponent import TextComponent
from GameWorkspace.Scripts import playerScript
from Engine.GameObject import GameObject


class Player(GameObject) :
    def __init__(self):
        super().__init__("Player")


    def start(self):
        Debug.PrintDebug("player start")

        self.addComponent(DrawCircleComponent(self, (255, 255, 255)))
        self.addComponent(TextComponent(self, "None"))
        self.addComponent(CircleColliderComponent(self))

        self.addComponent(playerScript.PlayerScript(self))

        super().start()

    def update(self,dt):
        super().update(dt)

    def end(self):
        Debug.PrintDebug("player end")