import Piece
import pygame

class Grid:

    def __init__(self, posX: int, posY: int, width: int, height: int):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.pieces = []
        self.clicked = False
        self.selected = None

    def addPiece(self, piece: Piece):
        self.pieces.append(piece)

    def removePiece(self, piece: Piece):
        if piece in self.pieces:
            self.pieces.remove(piece)

    def getOnMousePiece(self):
        list = [None]
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), 32*piece.getpatternY(), 32*piece.getpatternX())
            if rect.collidepoint(pygame.mouse.get_pos()):
                list.append(piece)
        return list[len(list)-1]

    def getOnMousePieceExcept(self, p: Piece):
        for piece in self.pieces:
            rect = pygame.Rect(piece.getPosX(), piece.getPosY(), 32*piece.getpatternY(), 32*piece.getpatternX())
            if rect.collidepoint(pygame.mouse.get_pos()) and p is not piece:
                return piece
        return None

    def placePiece(self, piece: Piece):
        if piece is None or self.getOnMousePieceExcept(piece) is not None:
            return
        import math
        (mouseX, mouseY) = pygame.mouse.get_pos()
        x = math.floor((mouseX-self.posX-piece.getpatternY()*32/2)/32)
        y = math.floor((mouseY-self.posY-piece.getpatternX()*32/2)/32)
        if x < -piece.getpatternY()+1 or x >= self.width/32 or y < -piece.getpatternX()+1 or y >= self.height/32:
            return
        piece.setPosX(self.posX+x*32)
        piece.setPosY(self.posY+y*32)
        return

    def renderFrame(self, window, backgroundColor):
        window.fill(backgroundColor)
        for x in range(0,int(self.width/32)):
            for y in range(0,int(self.height/32)):
                pygame.draw.line(window, (255, 255, 255), (self.posX + x * 32, self.posY + y * 32), (self.posX + (x + 1) * 32, self.posY + y * 32))
                pygame.draw.line(window, (255, 255, 255), (self.posX + x * 32, self.posY + y * 32), (self.posX + x * 32, self.posY + (y + 1) * 32))
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(self.posX, self.posY, self.width+1, self.height+1), 1)
        for piece in self.pieces:
            piece.render(window)
        pygame.display.flip()

    def updateFrame(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                    self.selected.setPosX(mouseX-self.selected.getpatternY()*32/2)
                    self.selected.setPosY(mouseY-self.selected.getpatternX()*32/2)