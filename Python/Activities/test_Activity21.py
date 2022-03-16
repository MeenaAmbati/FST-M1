import pytest

# Additon test
def test_addition():
	
    # Initialize two numbers
	num1 = 20
	num2 = 30
    
	# Add them
	sum = num1 + num2

	# Assertion
	assert sum == 25

# Subtraction test
def test_subtraction():
  
	# Initialize two numbers
	num1 = 60
	num2 = 45
    
	# Subtract them
	diff = num1 - num2

	# Assertion
	assert diff == 15

# Multiplication test
def test_multiplication():
  
	# Initialize two numbers
	num1 = 4
	num2 = 30
    
	# Multiply them
	prod = num1 * num2

	# Assertion
	assert prod == 100

# Division test
def test_division():
  
	# Initialize two numbers
	num1 = 500
	num2 = 10
    
	# Divide them
	quot = num1 / num2

	# Assertion
	assert quot == 20