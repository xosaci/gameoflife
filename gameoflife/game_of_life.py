import gameoflife.board as board
import matplotlib.pyplot as plt

#window = cv2.namedWindow('Game of life', cv2.WINDOW_NORMAL)

# Create the board and update it.
board = board.Board((80,80,5))
fig=plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_box_aspect((80,80,5))
fig.subplots_adjust(top=2, left=-1, right=2, bottom=-1, wspace=0, hspace=0)


_=0
while 1:
    board.update()

    array=board._board
    ax.voxels(array)
    ax.margins(0, tight=True)
    plt.pause(1)
    ax.cla()
