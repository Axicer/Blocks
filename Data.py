import Piece
import pygame
from copy import copy as cp
import Settings

TILECOLOR_BLUE = Piece.TileColor("blue.png")
TILECOLOR_RED = Piece.TileColor("red.png")
TILECOLOR_GREEN = Piece.TileColor("green.png")
TILE_BLUE = Piece.Tile(TILECOLOR_BLUE, False)
TILE_RED = Piece.Tile(TILECOLOR_RED, False)
TILE_GREEN = Piece.Tile(TILECOLOR_GREEN, False)

PIECE_R_RIGHT = Piece.Piece(
                [
                    [
                        cp(TILE_BLUE),
                        cp(TILE_BLUE),
                        None
                    ], [
                        None,
                        cp(TILE_BLUE),
                        cp(TILE_BLUE)
                    ]
                ],
                2, 3, 0, 0)
PIECE_R_LEFT = Piece.Piece(
                [
                    [
                        None,
                        cp(TILE_RED),
                        cp(TILE_RED)
                    ], [
                        cp(TILE_RED),
                        cp(TILE_RED),
                        None
                    ]
                ],
                2, 3, 2*Settings.GRID_RES, 1*Settings.GRID_RES)
PIECE_LONG = Piece.Piece(
                [
                    [
                        cp(TILE_GREEN),
                        cp(TILE_GREEN),
                        cp(TILE_GREEN),
                        cp(TILE_GREEN)
                    ]
                ],
                1, 4, 2 * Settings.GRID_RES, 0 * Settings.GRID_RES)

BACKGROUND_IMAGE = pygame.image.load("res/img/background.jpg")
