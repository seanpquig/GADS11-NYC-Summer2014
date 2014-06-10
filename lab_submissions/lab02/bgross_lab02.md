## Python Data Structures

## Code Commenting Exercise

In order to really understand fundamentals (and to be a great programmer/data scientist), it's absolutely essential to comment your code in order to understand what it is doing.

Below we will go through a brief introduction to each data structure in python. For each line, run the command in python, and write a comment above the line to explain what it does.

### Strings

* A string is a container of characters.
* Python strings are immutable, meaning they cannot change once assigned.

		python
		# This is a comment!
		
		# Storing a string to the variable s
		s = "Hello world, world"
		
		#printing the type. It shows 'str' which means it is a string type
		print type(s)
		
		# printing the number of characters in the string.
		print len(s)

		# Python gave me an error below! I guess we can't change individual parts of a string 		# this way.
		s[0] = 'h'
		
		#replace the word "world" (both of them) with the word "python" and assign to s2
		s2 = s.replace("world", "python")
		
		#replace the word "Hello" with the word "monty" and assign it to variable s3
		s3 = s2.replace("Hello","monty")
		
		#print the variable s
		print s
		
		#print the variable s2
		print s2
		
		#print the variable s3
		print s3
		
		#print the `char` elements from the 6th element, including the 10th (starting with 0)
		print s[6:11]
		
		#print from the 6th to, and including, the last element
		print s[6:]
		
		#print the 2nd to last 'char' to the end
		print s[-2:]
		
		#concatenate the string variable with a space and the variable s3 & assign to var s4
		s4 = s + ' ' + s3
		
		#print the variable s4
		print s4
		
		#return the index of the beginning of the first occurrence of the word "world."
		print s4.find('world')
		
		#assign the values 10, and 20.3 to the variables {0} and {1}, and then print to screen
		print 'A string with value {0} and {1}'.format(10,20.3)
		
		#access python documentation (inline) for the class str
		help(str)

### Lists

* A list is a container of objects.
* They do not need to be the same
* Mutable

		python
		
		#assign the variable values a list
		values = ['1',2,3.0,False]
		
		#print the number of elements in the list `values`
		print len(values)
		
		#print the type of `values` , i.e. list
		print type(values)
		
		#print the values of the list
		print values
		
		#print the 2nd value (or the 1th item) of the `values` list
		print values[1]
		
		#print the first 3 items in values (0, 1, 2)
		print values[:3]
		
		#print the 2th element (3rd) to the end
		print values[2:]
		
		#assign the variable l, and empty initialized list 
		l = []
		
		#append l (put the  value at the end) with the integer 8, inlace (w/o assignment)
		l.append(8)
		
		#append l (put the  value at the end) with the integer 10, inlace (w/o assignment)
		l.append(10)
		
		#...again... with 10
		l.append(10)
		
		#...again... with 12
		l.append(12)
		
		#print the list l
		print l
		
		#remove the first number occurrence of the number 10
		l.remove(10)
		
		#print the list l
		print l
		
		#remove the 0th element of the list l (by passing the first value of l)
		l.remove(l[0])
		
		#pring the list l
		print l
		
		#create a range from 0, excluding 10, by a step of 2
		l = range(0,10,2)

		#print the list l, [0, 2, 4, 6, 8]
		print l
		
		#assign the variable l, a range, from -5, 5 excluding, 5
		l = range(-5,5)
		
		#print l, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
		
		
		#print the variable l
		print l
		
		#assign the variable line the tex provided
		line = "This is a    \t list -      \t of strings"
		
		#print the length of the list, 3
		print len(line.split('\t'))
		
		#split the sentence into a list, with breakpoints at \t'p
		print line.split('\t')
		
		#iterator creating a list with 10 elements, each cell with 'add another field'
		print ['add another field' for i in range(10)]
		
		#assign the variable l with a arrange, -5 to 5, 5 not included
		l = range(-5,5)
		
		#print the range
		print l
		
		#reverse the list, and then print it [4, 3, ... , -4, -5]
		print l.sort(reverse=True)
		
		#print the already reversed list, [4, 3, ..., -4, -5]
		print l
		
		

###Tuples

* Sequence of objects, like lists, but immutable

```python

		#assign the variable t a tuple of values, 10, 40.0 and "A"
		t = (10,40.0,"A")
		
		#print out the type of `t` (tuple) and its length (3)
		print type(t), len(t)
		
		#error, tuple does not support assignment
		t[1] = 'B'
```

###Dictionaries

* A flexible collection of {key: value} pairs.
* Also called associative arrays or hash maps in other languages.

```python
		
		#initiate an empty dict
		data = {}
		
		#assign a key value 'k1' to the value of True
		data['k1'] = True
		
		assign a key value 'x2' to the value of 2
		data['x2'] = 2
		
		assign the key value 100 to the value of 3.0
		data[100] = 3.0
		
		#print the key and value pairings of data
		print data
		
		print the len of key, value combinations (3)
		print len(data), type(data)
		
		assign the key value 'k4' a value of 100
		data['k4'] = 100
		
		#recreate a new dictionary (garbage collect the old with new pairings
		data = {'number': 10, 1:'string'}
		
		#assign the key value 'c' with a list [1, 2, 3, 4]
		data['c'] = [1,2,3,4]
		
		print the dictionary
		print data
		
		print the value for the '1'th key in the dictionary
		print data[1]
		
		#print the 3rd element of the key value (a list) 'd'
		print data['c'][3]
		
		print the value pairing for the key 'data'
		print data['number']
```

###Classes

* Almost everything in python fits into a class
* You can also make classes on your own!

```python
class Car():
    def __init__(self, model='Ford', wheels = 4.):
        self.model = model
        self.running = False
        if wheels < 0.:
        	print "Can't have negative wheels, punk!"
        	self.wheels = 4
        else: 
        	self.wheels = wheels
    def start(self):
    	if self.running != True:
	        print 'The car started!'
			self.running = True
	    else:
	        print 'The car is already running!'
    def stop(self):
    	if self.running == True:
	        print 'The car stopped!'
			self.running = False
	    else:
	        print 'The car was not running!'
	        

ford = Car()
nissan = Car(model = 'Nissan')
ford.running
ford.start()
ford.running
nissan.running
nissan.stop()
```

## Lab Work

1. Change the Car class to have a default of 4 wheels, but can be set to any number
2. **Extra** if the car is told it has less than 0 wheels, make sure it sets to 0 and prints out that you can't have negative wheels on a car.
3. in lab_submissions/lab02/your_folder, submit a python file with all of your commented code from above, and the modifications you made to the Car class.