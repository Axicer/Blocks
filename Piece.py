class TileColor:

    def __init__(self, path):
        import pygame
        self.path = path
        self.img = pygame.transform.scale(pygame.image.load("res/img/"+path), (32,32))

    def getImage(self):
        return self.img

    def getPath(self):
        return self.path

class Tile:

    def __init__(self, color: TileColor, glow: bool):
        self.glow = glow
        self.color = color
        self.piece = None

    def setGlowing(self, glow: bool):
        self.glow = glow

    def isGlowing(self):
        return self.glow

    def setColor(self, color: TileColor):
        self.color = color

    def getColor(self):
        return self.color

    def getPiece(self):
        return self.piece

    def setPiece(self, piece):
        self.piece = piece

class Piece:

    def __init__(self, pattern, patternX: int, patternY: int, x: int, y: int):
        self.pattern = pattern
        self.patternX = patternX
        self.patternY = patternY
        self.x = x
        self.y = y

    def getpattern(self):
        return self.pattern

    def setpattern(self, pattern, patternX: int, patternY: int):
        self.pattern = pattern
        self.patternX = patternX
        self.patternY = patternY

    def getpatternX(self):
        return self.patternX

    def getpatternY(self):
        return self.patternY

    def setPosX(self, x: int):
        self.x = x

    def setPosY(self, y: int):
        self.y = y

    def getPosX(self):
        return self.x

    def getPosY(self):
        return self.y

    def setPos(self, x: int, y: int):
        self.setPosX(x)
        self.setposY(y)

    def render(self, window):
        for x in range(0, self.patternX):
            for y in range(0, self.patternY):
                t = self.pattern[x][y]
                if t is not None:
                    t.setPiece(self)
                    window.blit(t.getColor().getImage(), (self.x+y*32, self.y+x*32))
