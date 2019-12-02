
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
import itertools


def solve2(expected_value):
	pairs = np.array(np.meshgrid(np.arange(100), np.arange(100))).T.reshape(-1, 2)
	input_data = np.loadtxt("input-2.txt", delimiter=",", dtype=int)
	matches = list(itertools.ifilter(lambda c: solve1(np.array(input_data, copy=True), c[0], c[1]) == expected_value, pairs))
	print("Output: [Noun: " + str(matches[0][0]) + " Verb: " + str(matches[0][1]) + "]")
	return matches[0][0] * 100 + matches[0][1]


def solve1(input_data, var_1, var_2):
	# Initial conditions
	input_data[1] = var_1
	input_data[2] = var_2
	i = 0

	# Iterations
	while (i+3) < len(input_data):
		if input_data[i] == 1:
			res = input_data[input_data[i+1]] + input_data[input_data[i+2]]
			input_data[input_data[i+3]] = res
		elif input_data[i] == 2:
			res = input_data[input_data[i+1]] * input_data[input_data[i+2]]
			input_data[input_data[i+3]] = res
		elif input_data[i] == 99:
			# print("End execution found in pos: ", str(i))
			return input_data[0]
		else:
			print("Not valid input data pos " + str(i) + ": " + str(input_data[i]))
			return 0
		# Sentence Jump
		i = i+4


if __name__ == '__main__':
	print("Solving quiz number 2")
	data = np.loadtxt("input-2.txt", delimiter=",", dtype=int)
	# output1 = solve1(data, 12, 2)
	# print("Result problem 1: "+str(output1))
	output2 = solve2(19690720)
	print("Result problem 2: "+str(output2))

