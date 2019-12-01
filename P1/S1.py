import numpy as np

# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass,
# divide by three, round down, and subtract 2.

# The Fuel Counter-Upper needs to know the total fuel requirement.
# To find it, individually calculate the fuel needed for the mass
# of each module (your puzzle input), then add together all the fuel values.

# Sol.: 3401852

# What is the sum of the fuel requirements for all of the modules on your spacecraft when
# also taking into account the mass of the added fuel?

# Sol.: 5099916


def fuel(mass):
	return mass // 3 - 2


def accumulative_fuel(mass, sum_value):
	result = fuel(mass)
	if result <= 0:
		# print("Exit value: " + str(sum_value))
		return sum_value
	else:
		return accumulative_fuel(result, sum_value+result)


def solve1(input_data):
	total_fuel = int(np.sum(fuel(input_data)))
	print("Total Fuel: " + str(total_fuel))


def solve2(input_data):
	print("Solving quiz number 2")
	total_sum = 0
	for value in input_data:
		return_val = accumulative_fuel(value, 0)
		total_sum += return_val
		# print(int(return_val))
	print("Total Accumulative Fuel: " + str(int(total_sum)))


if __name__ == '__main__':
	print("Solving quiz number 1")
	data = np.loadtxt("input.txt")
	solve1(data)
	solve2(data)
