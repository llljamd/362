def fullName(first, last):
	try:
		if len(first) > 0 and len(last) > 0:
			return first + " " + last
	
	except:
		raise Exception("Enter a valid name.")
