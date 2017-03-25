import pygame
import Piece
import Data
import Grid

WIDTH = 720
HEIGHT = 480


class Main:

    def __init__(self, title):
        self.title = title
        self.clock = pygame.time.Clock()
        self.grid = Grid.Grid(150, 50, 32 * 10, 32 * 10)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(self.title)

    def main(self):
        while True:
            self.grid.updateFrame()
            self.grid.renderFrame(self.screen, (72, 72, 72))
            self.clock.tick(60)

    def init(self):
        self.grid.addPiece(Piece.Piece([[Data.TILE_BLUE, Data.TILE_BLUE, None], [None, Data.TILE_BLUE, Data.TILE_BLUE]], 2, 3, 0, 0))
        self.grid.addPiece(Piece.Piece([[None, Data.TILE_RED, Data.TILE_RED], [Data.TILE_RED, Data.TILE_RED, None]], 2, 3, 2*32, 1*32))
        self.grid.addPiece(Piece.Piece([[Data.TILE_GREEN, Data.TILE_GREEN, Data.TILE_GREEN, Data.TILE_GREEN]], 1, 4, 2 * 32, 0 * 32))
        self.main()

if __name__ == '__main__':
    Main("Blocks").init()
