from Engine.Components.BoxColliderComponent import BoxColliderComponent
from Engine.Components.DrawRectComponent import DrawRectComponent
from Engine.GameObject import GameObject


class Barrier(GameObject) :
    def start(self):
        self.addComponent(BoxColliderComponent(self))
        self.addComponent(DrawRectComponent(self,(255,255,255)))

