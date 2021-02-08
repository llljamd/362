def avg(x):
	total = 0

	try:
		for i in range(0, len(x)):
			total = total + x[i]
	
		return total / len(x)

	except ZeroDivisionError:
		return "No values."

	except:
		return "Error, not all numbers"
