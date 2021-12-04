#!/usr/local/bin/python3

f = open('input.txt', 'r')
# f = open('test_input.txt', 'r')

data = f.readlines()

def bin2string(data):
	s = ''
	for i in range(len(data)):
		s += str(data[i])
	return s

def calculate_gamma_epsilon(data):
	# Set up lists ahead of time
	gamma = [0]*(len(data[0])-1)
	epsilon = [1]*(len(data[0])-1)
	zeroes = [0]*(len(data[0])-1)
	ones = [0]*(len(data[0])-1)
	s_gamma = ''
	s_epsilon = ''

	# Find whether zero or one is more common per column
	for j in range(len(data)):
		for k in range(len(data[j])):
			if data[j][k] == '0':
				zeroes[k] += 1
			if data[j][k] == '1':
				ones[k] += 1

	# Create the gamma and epsilon values by comparing 0s and 1s
	for i in range(len(data[0])-1):
		if ones[i] > zeroes[i]:
			gamma[i] = 1
			epsilon[i] = 0

	return [bin2string(gamma), bin2string(epsilon)]

ge = calculate_gamma_epsilon(data)
int_gamma = int(ge[0], 2)
int_epsilon = int(ge[1], 2)

print("Gamma is:", int_gamma)
print("Epsilon is:", int_epsilon)
print("Power consumption is:", int_gamma*int_epsilon)

## Part two
def oxy_gamma(data):
	# Set up lists ahead of time
	gamma = [0]*(len(data[0])-1)
	epsilon = [1]*(len(data[0])-1)
	zeroes = [0]*(len(data[0])-1)
	ones = [0]*(len(data[0])-1)
	s_gamma = ''
	s_epsilon = ''

	# Find whether zero or one is more common per column
	for j in range(len(data)):
		for k in range(len(data[j])):
			if data[j][k] == '0':
				zeroes[k] += 1
			if data[j][k] == '1':
				ones[k] += 1

	# Create the gamma and epsilon values by comparing 0s and 1s
	for i in range(len(data[0])-1):
		if ones[i] == zeroes[i]:
			gamma[i] = 1
		elif ones[i] > zeroes[i]:
			gamma[i] = 1
			epsilon[i] = 0

	return bin2string(gamma)

def co2epsilon(data):
	# Set up lists ahead of time
	gamma = [0]*(len(data[0])-1)
	epsilon = [1]*(len(data[0])-1)
	zeroes = [0]*(len(data[0])-1)
	ones = [0]*(len(data[0])-1)
	s_gamma = ''
	s_epsilon = ''

	# Find whether zero or one is more common per column
	for j in range(len(data)):
		for k in range(len(data[j])):
			if data[j][k] == '0':
				zeroes[k] += 1
			if data[j][k] == '1':
				ones[k] += 1

	# Create the gamma and epsilon values by comparing 0s and 1s
	for i in range(len(data[0])-1):
		if ones[i] == zeroes[i]:
			epsilon[i] = 0
		elif ones[i] > zeroes[i]:
			gamma[i] = 1
			epsilon[i] = 0

	return bin2string(epsilon)

def oxy_data(data, value, start_point = 0):
	if len(data) == 1:
		return data
	local_data = data.copy()
	for i in reversed(range(len(local_data))):
		if ((int(local_data[i][start_point])) != int(value)):
			local_data.pop(i)
			if len(local_data) == 1: return local_data
			return oxy_data(local_data, value, start_point)
	return oxy_data(data,
		oxy_gamma(data)[start_point+1],
		start_point+1)

def co2data(data, value, start_point = 0):
	if len(data) == 1:
		return data
	local_data = data.copy()
	for i in reversed(range(len(local_data))):
		if ((int(local_data[i][start_point])) != int(value)):
			local_data.pop(i)
			if len(local_data) == 1: return local_data
			return co2data(local_data, value, start_point)
	return co2data(data,
		co2epsilon(data)[start_point+1],
		start_point+1)

oxygen = int(bin2string(oxy_data(data, int(ge[0][0]))), 2)
print("Oxygen level is:", oxygen)

co2 = int(bin2string(co2data(data, int(ge[1][0]))), 2)
print("Oxygen level is:", co2)

print("Life support rating is:", oxygen*co2)
