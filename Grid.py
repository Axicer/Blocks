import Piece
import pygame
import Settings
import Data
import Timer


class Grid:

    def __init__(self, posX: int, posY: int, width: int, height: int, window):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.pieces = []
        self.clicked = False
        self.selected = None
        self.timer = Timer.Timer(5, 0, 0, 0, window)
        self.timer.start()

    def addPiece(self, piece: Piece):
        self.pieces.append(piece)

    def removePiece(self, piece: Piece):
        if piece in self.pieces:
            self.pieces.remove(piece)

    def getOnMousePiece(self):
        list = [None]
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), Settings.GRID_RES*piece.getpatternY(), Settings.GRID_RES*piece.getpatternX())
            if rect.collidepoint(pygame.mouse.get_pos()):
                list.append(piece)
        return list[len(list)-1]

    def getOnMousePieceExcept(self, p: Piece):
        list = [None]
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), Settings.GRID_RES*piece.getpatternY(), Settings.GRID_RES*piece.getpatternX())
            if rect.collidepoint(pygame.mouse.get_pos()) and p is not piece:
                return list.append(piece)
        return list[len(list)-1]

    def placePiece(self, piece: Piece):
        if piece is None or self.getOnMousePieceExcept(piece) is not None:
            return
        import math
        (mouseX, mouseY) = pygame.mouse.get_pos()
        x = math.floor((mouseX-self.posX-piece.getpatternY()*Settings.GRID_RES/2)/Settings.GRID_RES)
        y = math.floor((mouseY-self.posY-piece.getpatternX()*Settings.GRID_RES/2)/Settings.GRID_RES)
        if x < -piece.getpatternY()+1 or x >= self.width/Settings.GRID_RES or y < -piece.getpatternX()+1 or y >= self.height/Settings.GRID_RES:
            return
        piece.setPosX(self.posX+x*Settings.GRID_RES)
        piece.setPosY(self.posY+y*Settings.GRID_RES)
        return

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
                if event.type == pygame.MOUSEMOTION:
                    if not self.clicked or self.selected is None:
                        continue
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    self.selected.setPosX(mouseX-self.selected.getpatternY()*Settings.GRID_RES/2)
                    self.selected.setPosY(mouseY-self.selected.getpatternX()*Settings.GRID_RES/2)
