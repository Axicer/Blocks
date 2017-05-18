import Settings
import pygame
import Data
import Grid
from copy import copy as cp

class Main:

    def __init__(self, title):
        self.title = title
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        self.grid = Grid.Grid(Settings.WIDTH / 2 - Settings.GRID_RES * Settings.GRID_X / 2, Settings.HEIGHT / 2 - Settings.GRID_RES * Settings.GRID_Y / 2, Settings.GRID_RES * Settings.GRID_X, Settings.GRID_RES * Settings.GRID_Y, self.screen)
        pygame.display.set_caption(self.title)

    def main(self):
        while True:
            self.grid.updateFrame()
            self.grid.renderFrame(self.screen, (72, 72, 72))
            self.clock.tick(60)

    def init(self):
        self.grid.addPiece(cp(Data.PIECE_R_RIGHT))
        self.grid.addPiece(cp(Data.PIECE_R_LEFT))
        self.grid.addPiece(cp(Data.PIECE_LONG_HORI))
        self.grid.addPiece(cp(Data.PIECE_SQUARED_4))
        self.grid.addPiece(cp(Data.PIECE_L_RIGHT_VERT))
        self.grid.addPiece(cp(Data.PIECE_L_LEFT_VERT))
        self.grid.addPiece(cp(Data.PIECE_L_LEFT_VERT))
        self.grid.addPiece(cp(Data.PIECE_L_LEFT_HORI))
        self.grid.addPiece(cp(Data.PIECE_L_RIGHT_HORI))
        self.grid.addPiece(cp(Data.PIECE_T))
        self.grid.addPiece(cp(Data.PIECE_T_REV))
        self.grid.addPiece(cp(Data.PIECE_R_RIGHT))
        self.grid.addPiece(cp(Data.PIECE_R_RIGHT))
        self.grid.addPiece(cp(Data.PIECE_LONG_HORI))
        self.grid.addPiece(cp(Data.PIECE_SQUARED_4))
        self.grid.addPiece(cp(Data.PIECE_L_LEFT_HORI))
        self.grid.addPiece(cp(Data.PIECE_T_REV))
        self.grid.addPiece(cp(Data.PIECE_L_LEFT_VERT_REV))
        self.grid.addPiece(cp(Data.PIECE_LONG_VERT))
        self.grid.addPiece(cp(Data.PIECE_SQUARED_4))
        self.grid.addPiece(cp(Data.PIECE_T_REV))
        self.grid.addPiece(cp(Data.PIECE_L_LEFT_HORI_REV))
        self.grid.addPiece(cp(Data.PIECE_SQUARED_4))
        self.grid.addPiece(cp(Data.PIECE_SQUARED_4))
        self.grid.addPiece(cp(Data.PIECE_SQUARED_4))
        self.main()

if __name__ == '__main__':
    pygame.font.init()
    Main("Blocks").init()
