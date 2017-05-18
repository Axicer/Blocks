from Piece import *
from copy import copy as cp

TILECOLOR_BLUE = TileColor("blue.png")
TILECOLOR_RED = TileColor("red.png")
TILECOLOR_GREEN = TileColor("green.png")
TILECOLOR_YELLOW = TileColor("yellow.png")
TILECOLOR_CYAN = TileColor("cyan.png")
TILECOLOR_GRAY = TileColor("gray.png")
TILECOLOR_ORANGE = TileColor("orange.png")
TILECOLOR_PINK = TileColor("pink.png")
TILECOLOR_PURPLE = TileColor("purple.png")
TILECOLOR_SILVER = TileColor("silver.png")

TILE_BLUE = Tile(TILECOLOR_BLUE)
TILE_RED = Tile(TILECOLOR_RED)
TILE_GREEN = Tile(TILECOLOR_GREEN)
TILE_YELLOW = Tile(TILECOLOR_YELLOW)
TILE_CYAN = Tile(TILECOLOR_CYAN)
TILE_GRAY = Tile(TILECOLOR_GRAY)
TILE_ORANGE = Tile(TILECOLOR_ORANGE)
TILE_PINK = Tile(TILECOLOR_PINK)
TILE_PURPLE = Tile(TILECOLOR_PURPLE)
TILE_SILVER = Tile(TILECOLOR_SILVER)

PIECE_SQUARED_4 = Piece(
    [
        [
            cp(TILE_GRAY),
            cp(TILE_GRAY)
        ],
        [
            cp(TILE_GRAY),
            cp(TILE_GRAY)
        ]
    ],
    2, 2, 0, 0
)

PIECE_L_RIGHT_VERT = Piece(
    [
        [
            cp(TILE_GREEN),
            None
        ],
        [
            cp(TILE_GREEN),
            None
        ],
        [
            cp(TILE_GREEN),
            cp(TILE_GREEN)
        ]
    ],
    3, 2, 0, 0
)

PIECE_L_LEFT_VERT = Piece(
    [
        [
            None,
            cp(TILE_PURPLE)
        ],
        [
            None,
            cp(TILE_PURPLE)
        ],
        [
            cp(TILE_PURPLE),
            cp(TILE_PURPLE)
        ]
    ],
    3, 2, 0, 0
)

PIECE_L_LEFT_VERT_REV = Piece(
    [
        [
            cp(TILE_PINK),
            cp(TILE_PINK)
        ],
        [
            cp(TILE_PINK),
            None
        ],
        [
            cp(TILE_PINK),
            None
        ]
    ],
    3, 2, 0, 0
)

PIECE_L_LEFT_HORI = Piece(
    [
        [
            cp(TILE_ORANGE),
            cp(TILE_ORANGE),
            cp(TILE_ORANGE)
        ],
        [
            None,
            None,
            cp(TILE_ORANGE)
        ]
    ],
    2, 3, 0, 0
)

PIECE_L_LEFT_HORI_REV = Piece(
    [
        [
            cp(TILE_ORANGE),
            None,
            None
        ],
        [
            cp(TILE_ORANGE),
            cp(TILE_ORANGE),
            cp(TILE_ORANGE)
        ]
    ],
    2, 3, 0, 0
)

PIECE_L_RIGHT_HORI = Piece(
    [
        [
            None,
            None,
            cp(TILE_PINK)
        ],
        [
            cp(TILE_PINK),
            cp(TILE_PINK),
            cp(TILE_PINK)
        ]
    ],
    2, 3, 0, 0
)

PIECE_R_RIGHT = Piece(
    [
        [
            cp(TILE_CYAN),
            cp(TILE_CYAN),
            None
        ], [
            None,
            cp(TILE_CYAN),
            cp(TILE_CYAN)
        ]
    ],
    2, 3, 0, 0
)

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
    2, 3, 0, 0
)

PIECE_LONG_HORI = Piece(
    [
        [
            cp(TILE_GREEN),
            cp(TILE_GREEN),
            cp(TILE_GREEN),
            cp(TILE_GREEN)
        ]
    ],
    1, 4, 0, 0
)
PIECE_LONG_VERT = Piece(
    [
        [
            cp(TILE_GRAY)
        ],
[
            cp(TILE_GRAY)
        ],
[
            cp(TILE_GRAY)
        ],
[
            cp(TILE_GRAY)
        ]
    ],
    4, 1, 0, 0
)

PIECE_T = Piece(
    [
        [
            cp(TILE_BLUE),
            cp(TILE_BLUE),
            cp(TILE_BLUE),
        ],
        [
            None,
            cp(TILE_BLUE),
            None
        ]
        ],
    2, 3, 0, 0
)

PIECE_T_REV = Piece(
    [
        [
            None,
            cp(TILE_RED),
            None
        ],
        [
            cp(TILE_RED),
            cp(TILE_RED),
            cp(TILE_RED),
        ],
        ],
    2, 3, 0, 0
)

BACKGROUND_IMAGE = pygame.image.load("res/img/background.jpg")
