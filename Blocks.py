import Settings
import pygame
import Piece
import Data
import Grid


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
        self.grid.addPiece(Piece.Piece([[Data.TILE_BLUE, Data.TILE_BLUE, None], [None, Data.TILE_BLUE, Data.TILE_BLUE]], 2, 3, 0, 0))
        self.grid.addPiece(Piece.Piece([[None, Data.TILE_RED, Data.TILE_RED], [Data.TILE_RED, Data.TILE_RED, None]], 2, 3, 2*Settings.GRID_RES, 1*Settings.GRID_RES))
        self.grid.addPiece(Piece.Piece([[Data.TILE_GREEN, Data.TILE_GREEN, Data.TILE_GREEN, Data.TILE_GREEN]], 1, 4, 2 * Settings.GRID_RES, 0 * Settings.GRID_RES))
        self.main()

if __name__ == '__main__':
    pygame.font.init()
    Main("Blocks").init()
