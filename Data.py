from Piece import *
from Settings import *
from copy import copy as cp

TILECOLOR_BLUE = TileColor("blue.png")
TILECOLOR_RED = TileColor("red.png")
TILECOLOR_GREEN = TileColor("green.png")
TILECOLOR_YELLOW = TileColor("yellow.png")

TILE_BLUE = Tile(TILECOLOR_BLUE, False)
TILE_RED = Tile(TILECOLOR_RED, False)
TILE_GREEN = Tile(TILECOLOR_GREEN, False)
TILE_YELLOW = Tile(TILECOLOR_YELLOW, False)

PIECE_R_RIGHT = Piece(
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
                2, 3, 0 * GRID_RES, 0 * GRID_RES)
PIECE_R_LEFT = Piece(
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
                2, 3, 2 * GRID_RES, 1 * GRID_RES)
PIECE_LONG = Piece(
                [
                    [
                        cp(TILE_GREEN),
                        cp(TILE_GREEN),
                        cp(TILE_GREEN),
                        cp(TILE_GREEN)
                    ]
                ],
                1, 4, 2 * GRID_RES, 0 * GRID_RES)
PIECE_U = Piece(
                [
                    [
                        cp(TILE_YELLOW),
                        None,
                        cp(TILE_YELLOW)
                    ],
                    [
                        cp(TILE_YELLOW),
                        cp(TILE_YELLOW),
                        cp(TILE_YELLOW)
                    ]
                ],
                2, 3, 4 * GRID_RES, 2 * GRID_RES)
PIECE_STRANGE_1 = Piece(
                [
                    [
                        cp(TILE_YELLOW),
                        cp(TILE_YELLOW),
                        cp(TILE_YELLOW)
                    ],
                    [
                        cp(TILE_YELLOW),
                        None,
                        cp(TILE_YELLOW)
                    ],
                    [
                        cp(TILE_YELLOW),
                        None,
                        None
                    ],
                    [
                        cp(TILE_YELLOW),
                        None,
                        None
                    ]
                ],
                4, 3, 8 * GRID_RES, 2 * GRID_RES)

BACKGROUND_IMAGE = pygame.image.load("res/img/background.jpg")
