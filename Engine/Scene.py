from abc import ABC


class Scene(ABC) :
    def __init__(self):
        self.GameObjects = []
        self.toBeRemoved = []
        self.Used = False

    def start(self):
        for go in self.GameObjects:
            go.start()
        self.Used = True


    def update(self,dt):

        for i in range(len(self.GameObjects)):
            self.GameObjects[i].update(dt)

        if(len(self.toBeRemoved) > 0) :
            self.rm()

    def addGameObject(self, gameObject):
        if self.Used :
            gameObject.start()
        self.GameObjects.append(gameObject)


    def  rm(self):
        for go in self.toBeRemoved :
            if go in self.GameObjects :
                go.end()
                self.GameObjects.remove(go)
        self.toBeRemoved.clear()

    def end(self):
        self.toBeRemoved.extend(self.GameObjects)


    def removeGameObject(self, gameObject):
        self.toBeRemoved.append(gameObject)