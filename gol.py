import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):

	return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def update(frameNum, img, grid, N, ):

	newGrid = grid.copy()
	for i in range(N):
		for j in range(N):

			total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
						grid[(i-1)%N, j] + grid[(i+1)%N, j] +
						grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
						grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

			if grid[i, j] == ON:
				if (total < 2) or (total > 3):
					newGrid[i, j] = OFF
			else:
				if total == 3:
					newGrid[i, j] = ON

	img.set_data(newGrid)
	grid[:] = newGrid[:]
	return img,

def ini_grid(grid,size, file_ini):
	file_handler = open(file_ini,'r').readlines()
	for i_line in range(0, size):
		for i_b in range(0,size):
			if file_handler[i_line][i_b] == '0':
				grid[i_line][i_b] = 0
			if file_handler[i_line][i_b] == '1':
				grid[i_line][i_b] = 255

	return grid

def show_gol(size, file_ini, time, updateInterval = 500, repeat = False):

	grid = np.array([])

	grid = randomGrid(size)

	grid = ini_grid(grid, size, file_ini = file_ini)
	itr_start = 0

	fig, ax = plt.subplots()
	img = ax.imshow(grid, interpolation='nearest')
	ani = animation.FuncAnimation(fig, update, fargs=(img, grid, size, ),
								frames = time,
								interval=updateInterval,
								save_count=time,
								repeat=repeat
								)

	plt.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Printing Conway's Game of Life")

    parser.add_argument("-i", "--inputfile", type=str, help="File with start grid")
    parser.add_argument("-s", "--size", type=int,  help="Size of the grid")
    parser.add_argument("-t", "--time", type=int,  help="Time of computations")

    args = parser.parse_args()
    show_gol(size = args.size, file_ini = args.inputfile, time = args.time, updateInterval = 500, repeat = False)
