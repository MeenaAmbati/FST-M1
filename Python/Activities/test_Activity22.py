import pytest

def test_addition():
	
	num1 = 20
	num2 = 30
    

	sum = num1 + num2

	
	assert sum == 25


def test_subtraction():
  
	
	num1 = 60
	num2 = 45
    
	
	diff = num1 - num2

	
	assert diff == 15


@pytest.mark.activity
def test_multiplication():
  
	
	num1 = 4
	num2 = 30
  
	prod = num1 * num2

	
	assert prod == 100


@pytest.mark.activity
def test_division():
  
	
	num1 = 500
	num2 = 10
    
	
	quot = num1 / num2


	assert quot == 20