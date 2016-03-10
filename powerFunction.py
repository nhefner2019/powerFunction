def power(base, exponent):
	
	tally = 0
	answer = 1
	while tally < exponent:
		answer = answer * base
		tally += 1
		
	print(answer)
		
	
	
#Main Program
base = int(raw_input("What will be your base? "))
exponent = int(raw_input("What will be your exponent? "))

power(base, exponent)