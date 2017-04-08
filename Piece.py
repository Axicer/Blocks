import Settings
import pygame


class TileColor:

    def __init__(self, path):
        import pygame
        self.path = path
        self.img = pygame.transform.scale(pygame.image.load("res/img/"+path), (Settings.GRID_RES, Settings.GRID_RES))

    def getImage(self):
        return self.img

    def getPath(self):
        return self.path


class Tile:

    def __init__(self, color: TileColor, glow: bool):
        self.glow = glow
        self.color = color
        self.piece = None
        self.x = 0
        self.y = 0

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

    def setXOffset(self, x: int):
        self.x = x

    def getXOffset(self):
        return self.x

    def setYOffset(self, y: int):
        self.y = y

    def getYOffset(self):
        return self.y

    def getRect(self):
        return pygame.Rect(
                self.piece.getPosX() + self.getXOffset() * Settings.GRID_RES,
                self.piece.getPosY() + self.getXOffset() * Settings.GRID_RES,
                self.piece.getPosX() + self.getXOffset() * Settings.GRID_RES + Settings.GRID_RES,
                self.piece.getPosY() + self.getYOffset() * Settings.GRID_RES + Settings.GRID_RES)

class Piece:

    def populateTiles(self):
        for x in range(0, self.patternX):
            for y in range(0, self.patternY):
                t = self.pattern[x][y]
                if t is not None:
                    t.setPiece(self)
                    t.setXOffset(x)
                    t.setYOffset(y)

    def __init__(self, pattern: object, patternX: object, patternY: object, x: object, y: object) -> object:
        self.pattern = pattern
        self.patternX = patternX
        self.patternY = patternY
        self.x = x
        self.y = y
        self.populateTiles()

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
                    window.blit(t.getColor().getImage(), (self.x+y*Settings.GRID_RES, self.y+x*Settings.GRID_RES))

    def getTiles(self):
        l = []
        for x in range(0, self.patternX):
            for y in range(0, self.patternY):
                t = self.pattern[x][y]
                if t is not None:
                    l.append(t)
        return l
