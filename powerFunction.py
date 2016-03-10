def power(base, exponent):
	
	tally = 0
	answer = 1
	while tally < exponent:
		answer = answer * base
		tally += 1
		
	return answer
		
	
	
#Main Program
base = int(raw_input("What will be your base? "))
exponent = int(raw_input("What will be your exponent? "))

answer = power(base, exponent)

print("Your base is {}. Your exponent is {}. The product is {}".format(base, exponent, answer))