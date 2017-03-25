import Piece
import pygame

TILECOLOR_BLUE = Piece.TileColor("blue.png")
TILECOLOR_RED = Piece.TileColor("red.png")
TILECOLOR_GREEN = Piece.TileColor("green.png")
TILE_BLUE = Piece.Tile(TILECOLOR_BLUE, False)
TILE_RED = Piece.Tile(TILECOLOR_RED, False)
TILE_GREEN = Piece.Tile(TILECOLOR_GREEN, False)

BACKGROUND_IMAGE = pygame.image.load("res/img/background.jpg")
