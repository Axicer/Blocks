import Piece
import pygame
import Settings
import Data
import Timer
import copy
import numpy


class Grid:

    def __init__(self, posX: int, posY: int, width: int, height: int, window):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.rows = int(height/Settings.GRID_RES)
        self.columns = int(width/Settings.GRID_RES)
        self.pieces = []
        self.clicked = False
        self.selected = None
        self.timer = Timer.Timer(5, 0, 0, 0, window)
        self.timer.start()
        self.grid = numpy.array([[0] * self.columns] * self.rows)

    def addPiece(self, piece: Piece):
        self.pieces.append(piece)

    def removePiece(self, piece: Piece):
        if piece in self.pieces:
            self.pieces.remove(piece)

    def getPiece(self, x, y):
        l = [None]
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), Settings.GRID_RES * piece.getpatternY(), Settings.GRID_RES * piece.getpatternX())
            if rect.collidepoint((x, y)):
                l.append(piece)
        return l[len(l)-1]

    def getOnMousePiece(self):
        l = [None]
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), Settings.GRID_RES*piece.getpatternY(), Settings.GRID_RES*piece.getpatternX())
            if rect.collidepoint(pygame.mouse.get_pos()):
                l.append(piece)
        return l[len(l)-1]

    def getOnMousePieceExcept(self, p: Piece):
        l = [None]
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), Settings.GRID_RES*piece.getpatternY(), Settings.GRID_RES*piece.getpatternX())
            if rect.collidepoint(pygame.mouse.get_pos()) and p is not piece:
                l.append(piece)
        return l[len(l)-1]

    def checkGridDone(self):
        for x in range(0, self.rows):
            for y in range(0, self.columns):
                if self.grid[x][y] == 0:
                    return False
        return True

    def placePiece(self, piece: Piece):
        if piece is None or self.getOnMousePieceExcept(piece) is not None:
            return

        import math
        (mouseX, mouseY) = pygame.mouse.get_pos()
        diffX = (mouseX-self.posX-piece.getpatternY()*Settings.GRID_RES/2)/Settings.GRID_RES
        diffY = (mouseY-self.posY-piece.getpatternX()*Settings.GRID_RES/2)/Settings.GRID_RES
        x = math.ceil(diffX) if math.ceil(diffX)-diffX < 0.5 else math.floor(diffX)
        y = math.ceil(diffY) if math.ceil(diffY)-diffY < 0.5 else math.floor(diffY)

        if x < -piece.getpatternY()+1 or x >= self.width/Settings.GRID_RES or y < -piece.getpatternX()+1 or y >= self.height/Settings.GRID_RES:
            return

        canPlace = True
        for tile in piece.getTiles():
            toffX, toffY = tile.getXOffset(), tile.getYOffset()
            if x+toffY < 0 or x+toffY > self.columns-1 or y+toffX < 0 or y+toffX > self.rows-1:
                continue
            if self.grid[y+toffX][x+toffY] == 1:
                canPlace = False
                break
        if canPlace:
            piece.setPosX(self.posX+x*Settings.GRID_RES)
            piece.setPosY(self.posY+y*Settings.GRID_RES)
            for tile in piece.getTiles():
                toffX, toffY = tile.getXOffset(), tile.getYOffset()
                if x+toffY < 0 or x+toffY > self.columns-1 or y+toffX < 0 or y+toffX > self.rows-1:
                    continue
                self.grid[y+toffX][x+toffY] = 1

    def deletePiece(self, piece: Piece):
        if piece is None:
            return

        import math
        (mouseX, mouseY) = pygame.mouse.get_pos()
        diffX = (mouseX - self.posX - piece.getpatternY() * Settings.GRID_RES / 2) / Settings.GRID_RES
        diffY = (mouseY - self.posY - piece.getpatternX() * Settings.GRID_RES / 2) / Settings.GRID_RES
        x = math.ceil(diffX) if math.ceil(diffX) - diffX < 0.5 else math.floor(diffX)
        y = math.ceil(diffY) if math.ceil(diffY) - diffY < 0.5 else math.floor(diffY)

        if x < -piece.getpatternY()+1 or x >= self.width/Settings.GRID_RES or y < -piece.getpatternX()+1 or y >= self.height/Settings.GRID_RES:
            return

        for tile in piece.getTiles():
            toffX, toffY = tile.getXOffset(), tile.getYOffset()
            if x+toffY < 0 or x+toffY > self.columns-1 or y+toffX < 0 or y+toffX > self.rows-1:
                continue
            self.grid[y+toffX][x+toffY] = 0

    def renderFrame(self, window, backgroundColor):
        window.fill(backgroundColor)
        window.blit(Data.BACKGROUND_IMAGE, (0,0))
        for piece in self.pieces:
            piece.render(window)
        for x in range(0, int(self.width/Settings.GRID_RES)):
            for y in range(0, int(self.height/Settings.GRID_RES)):
                pygame.draw.line(window, (255, 255, 255), (self.posX + x * Settings.GRID_RES, self.posY + y * Settings.GRID_RES), (self.posX + (x + 1) * Settings.GRID_RES, self.posY + y * Settings.GRID_RES))
                pygame.draw.line(window, (255, 255, 255), (self.posX + x * Settings.GRID_RES, self.posY + y * Settings.GRID_RES), (self.posX + x * Settings.GRID_RES, self.posY + (y + 1) * Settings.GRID_RES))
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(self.posX, self.posY, self.width+1, self.height+1), 1)
        textsurface = self.timer.font.render(str(self.timer.getMinutes()) + ":" + str(self.timer.getSeconds()), False, (255, 255, 255))
        window.blit(textsurface, (Settings.WIDTH/2-25, 0))
        pygame.display.flip()

    def updateFrame(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.timer.stop()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.clicked = False
                    self.placePiece(self.selected)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected = self.getOnMousePiece()
                    self.clicked = True
                    self.deletePiece(self.selected)
                if event.type == pygame.MOUSEMOTION:
                    if not self.clicked or self.selected is None:
                        continue
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    self.selected.setPosX(mouseX - self.selected.getpatternY() * Settings.GRID_RES / 2)
                    self.selected.setPosY(mouseY - self.selected.getpatternX() * Settings.GRID_RES / 2)
