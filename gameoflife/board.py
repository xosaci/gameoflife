import numpy

class Board:
    """
    Creates a squared board.

    :param board_shape: The shape of the board.
    :param patch_shape: The shape of the patch which computes the number of neighbors.
    """

    def __init__(self, board_shape: tuple = (100, 100, 100), patch_shape: tuple = (3, 3, 3)):
        self._board = numpy.random.randint(25, size=board_shape, dtype=numpy.int8)
        self._board = numpy.where(self._board > 1, 0, self._board)
        self._patches_shape = patch_shape

    @property
    def board(self):
        return self._board

    def update(self):
        """
        Computes the rules of the game of life.

        If 2 or 3 pixels around a valid pixel are valid, then the pixel stays alive.
        If 3 pixels around an invalid pixel are valid, this pixel becomes alive.
        """
        entry=numpy.pad(self._board, self._patches_shape[0] // 2)
        pix_by_ptch = numpy.sum(numpy.lib.stride_tricks.sliding_window_view(entry, (3,3,3), axis=(-1,-2,-3)), axis=(-1,-2,-3))
        self._board = (((pix_by_ptch == 4)) & ~self._board) | ((
            (pix_by_ptch == 3)
        ) & self._board)

        #self._board = ((pix_by_ptch == 3))
