
# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
# To run one, start by looking at the first integer (called position 0). Here, you will
# find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example,
# 99 means that the program is finished and should immediately halt.
# Encountering an unknown opcode means something went wrong.

# Opcode 1 adds together numbers read from two positions and stores the result in a third position.
# The three integers immediately after the opcode tell you these three positions

# Opcode 2 multiplies the two inputs instead of adding them.
# Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

import numpy as np


def solve1(input_data):
	data_lenght = len(input_data)
	i = 0
	# Initial conditions
	input_data[1] = 12
	input_data[2] = 2
	while (i+3) < data_lenght:
		if input_data[i] == 1:
			res = input_data[input_data[i+1]] + input_data[input_data[i+2]]
			input_data[input_data[i+3]] = res
		elif input_data[i] == 2:
			res = input_data[input_data[i+1]] * input_data[input_data[i+2]]
			input_data[input_data[i+3]] = res
		elif input_data[i] == 99:
			print("End execution found in pos: ", str(i))
		else:
			print("Not valid input data pos " + str(i) + ": " + str(input_data[i]))
			exit(1)

		i = i+4

	print("Value at last: " + str(input_data[0]))


if __name__ == '__main__':
	print("Solving quiz number 2")
	data = np.loadtxt("input-2.txt", delimiter=",", dtype=int)
	print(len(data))
	solve1(data)
