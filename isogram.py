#concept, isogram

def isogram_detector(string):
	lower_string = string.lower()
	if len(set(lower_string)) == len(lower_string):
		return True
	else:
		return False

