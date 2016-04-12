#---------------Function----------------------
def power(base, exponent):
	
	if exponent == 0:
		return 1
	
	result = base * power(base, exponent - 1)
		
	return result
	

def int_input(question):
	
	answer = raw_input(question)
	
	try:
		#terminating case
		answer = int(answer)
		return answer
	except ValueError:
		#recursive call
		return int_input("That is not an integer; try again. ")
		
def float_input(question):
	
	answer = raw_input(question)
	
	try:
		#terminating case
		answer = float(answer)
		return answer
	except ValueError:
		#recursive call
		return float_input("That is not a float; try again. ")





#---------------Main Program------------------------	
base = float_input("What will be your base? ")
exponent = int_input("What will be your exponent? ")

product = power(base, exponent)

print("Your base is {}. Your exponent is {}. The product is {}".format(base, exponent, product))