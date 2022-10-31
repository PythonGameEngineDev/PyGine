from Engine.Component import Component
from Engine.Transform import Transform


class BoxComponent(Component) :
    def __init__(self,parent) :
        super().__init__(parent)
        self.parent = parent
        self.transform = parent.transform


    def collide(self,o):

        if (o.transform.position.x+o.transform.scale.x > self.transform.position.x > o.transform.position.x ) or \
                (self.transform.position.x+self.transform.scale.x > o.transform.position.x > self.transform.position.x ):
            if (o.transform.position.y + o.transform.scale.y > self.transform.position.y > o.transform.position.y) or \
                    (self.transform.position.y + self.transform.scale.y > o.transform.position.y > self.transform.position.y):
                return True
        return False
