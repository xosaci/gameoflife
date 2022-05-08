import cv2
import gameoflife.board as board

window = cv2.namedWindow('Game of life', cv2.WINDOW_NORMAL)

# Create the board and update it.
board = board.Board((90,160))

while cv2.getWindowProperty('Game of life', cv2.WND_PROP_VISIBLE):
    board.update()
    cv2.imshow('Game of life', board.board.astype(float))
    cv2.waitKey(100)
