
def calculate_sum(numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum

numList = [20, 60, 40, 80]

result = calculate_sum(numList)

print("The sum of all the elements is: " + str(result))