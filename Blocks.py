import pygame
import Piece
import Data
import Grid

class Main:

    def __init__(self, bounds, title, backgroundColor):
        self.bounds = bounds
        self.title = title
        self.backgroundColor = backgroundColor;


    """-------------"""
    """     MAIN    """
    """-------------"""

    def main(self):
        while True:
            self.grid.updateFrame()
            self.grid.renderFrame(self.screen, self.backgroundColor)
            self.clock.tick(60)

    def init(self):
        print("Program start.")
        self.screen = pygame.display.set_mode(self.bounds)
        pygame.display.set_caption(self.title)
        self.screen.fill(self.backgroundColor)
        self.clock = pygame.time.Clock()
        self.grid = Grid.Grid(150,50,32*10,32*10)
        self.grid.addPiece(Piece.Piece([[Data.TILE_BLUE, Data.TILE_BLUE, None], [None, Data.TILE_BLUE, Data.TILE_BLUE]], 2, 3, 0, 0))
        self.grid.addPiece(Piece.Piece([[None, Data.TILE_RED, Data.TILE_RED], [Data.TILE_RED, Data.TILE_RED, None]], 2, 3, 2*32, 1*32))
        self.grid.addPiece(Piece.Piece([[Data.TILE_GREEN, Data.TILE_GREEN, Data.TILE_GREEN, Data.TILE_GREEN]], 1, 4, 2 * 32, 0 * 32))
        self.main()

if __name__ == '__main__':
    Main((3*256,2*256), "Blocks", (0,0,0)).init()