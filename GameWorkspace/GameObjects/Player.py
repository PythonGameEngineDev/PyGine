from Engine import Debug
from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.CircleColliderComponent import CircleColliderComponent
from Engine.Components.DrawCircleComponent import DrawCircleComponent
from Engine.Components.TextComponent import TextComponent
from Engine.Vector3 import Vector3
from GameWorkspace.Scripts.playerScript import PlayerScript
from Engine.GameObject import GameObject


class Player(GameObject) :

    def start(self):
        Debug.PrintDebug("player start")

        self.transform.position = Vector3(0,0, 0)
        self.transform.scale = Vector3(100,100,100)
        self.AttachCamera(True)

        self.addComponent(DrawCircleComponent(self, (255, 255, 255),self.transform.scale.x))
        self.addComponent(TextComponent(self, "your text here"))
        self.addComponent(CircleColliderComponent(self))
        self.addComponent(PlayerScript(self))

