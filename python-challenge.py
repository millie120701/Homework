#num of students, calculates and prints a string for proposed number of classes
#max 30
#2 classes minimum
#as even as possible
#hire as little as possible

#We want big classes and minimal teachers
import math 

def classes(students):
	#place to store our classes
	class_dict = {}
	if students <= 30:
		class_dict["class 1"] = math.ceil(students/2)
		class_dict["class 2"] = students - math.ceil(students/2)
	else:
		#num of classes, rounded up e.g. math.ceil(31/30) would be 2
		num_classes = math.ceil(students / 30)
		#num in first class e.g. 31//2 = 16
		num_in_class = (students // num_classes)
		#remaining is modulus e.g. 31 % 16 = 15
		remaining_students = students % num_classes
		print(remaining_students)
		#we must allocate the remaining students a class
		for i in range(1, num_classes + 1): 
			print(i)
			if i <= remaining_students:
				#when we have remaining students that need to be added
				#once i > remaining_students, we know we have added 
				#all remaining students to the classes
			    class_dict[f"Class {i}"] = num_in_class + 1
			    print(class_dict)
			else:
				#i > remaining students, no more students to add to the 
				#num in class 
				class_dict[f"Class {i}"] = num_in_class
				print(class_dict)

		return f"Proposed Allocation: {num_classes} classes\n{class_dict}"
























