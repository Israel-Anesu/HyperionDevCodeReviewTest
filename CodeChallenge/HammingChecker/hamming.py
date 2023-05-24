# Python Hamming Checker

def calc_redundant_bits(m):
	# The formula 2 ^ r >= m + r + 1 is used to calculate the no of redundant bits.	
	for i in range(m):
		if(2**i >= m + i + 1):
			return i

def pos_redundant_bits(data, r):
	# Redundancy bits are placed at the positions which correspond to the power of 2.
	j = 0
	k = 1
	m = len(data)
	res = ''

	# If the position has the power of 2 then insert '0' else append the data
	for i in range(1, m + r+1):
		if(i == 2**j):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1

	# The result is reversed since positions are counted backwards.
	return res[::-1]


def calc_parity_bits(arr, r):
	n = len(arr)

	# For finding rth parity bit, iterate over 0 to r - 1
	for i in range(r):
		val = 0
		for j in range(1, n + 1):			
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])				

		# String Concatenation		
		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
	return arr


def detect_error(arr, nr):
	n = len(arr)
	res = 0

	# Calculate parity bits again
	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])

		# Creating a binary number by appending parity bits together.
		res = res + val*(10**i)

	#Converting binary to decimal
	return int(str(res), 2)


# Enter the data to be transmitted
data = '1011001'

# Calculate the no of Redundant Bits Required
m = len(data)
r = calc_redundant_bits(m)

# Determine the positions of Redundant Bits
arr = pos_redundant_bits(data, r)

# Determine the parity bits
arr = calc_parity_bits(arr, r)

# Data to be transferred
print("Data: " + arr)

arr = '10101001110'
print("Error Data: " + arr)
correction = detect_error(arr, r)
if(correction == 0):
	print("No Error Detected!.")
else:
	print("Error Index: ",len(arr)-correction + 1)