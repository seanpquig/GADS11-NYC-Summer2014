#########################################################
#### Name: lab02a_robertwest.py
#### Description: Code Commenting Exercise
#### Author: Robert D. West
#### Date: 6.7.2014

#########################################################
######################## Strings ########################
#########################################################

# A string is a container of characters.
# Python strings are immutable, meaning they cannot change once assigned.

# This is a comment!
# Storing a string to the variable s
s = "Hello world, world"
# printing the type. It shows 'str' which means it is a string type
print type(s)
# printing the number of characters in the string.
print len(s)
# Python gave me an error below! I guess we can't change individual parts of a string this way.
# s[0] = 'h'
# from here continue writing a comment for each line explaining what the following line does.

# exactly what is says on the tin. this will copy the string 's' and store it in 's2' as well as making the modiication that all instances of the word 'world' wil be replaced with 'python' within the string
s2 = s.replace("world", "python")
# the same as the line above, this time all substrings 'Hello' will be replaced with 'monty'
s3 = s2.replace("Hello","monty")
# prints the string 's'
print s
# prints the string 's2'
print s2
# prints the string 's3'
print s3
# prints the a subsection of the string from the 7th to the 11th element
print s[6:11]
# prints the a subsection of the string from the 7th element to the end
print s[6:]
# prints from the 2nd to last element to the end 
print s[-2:]
# concatenates the strings s and s3 as well as addding a space between them
s4 = s + ' ' + s3
# prints 's4'
print s4
# finds the first occurence of the subsection of the string 'world' and returns an index pointing to the beginning of that word, of the subsection is not in the string then -1 will be returned
print s4.find('world')
# here the method 'format' on the class object string will replace the respective instances of {0}, {1}, etc.. with the information given to the format method, this could be integers, floats, strings.. here we pass an integer then a float
print 'A string with value {0} and {1}'.format(10,20.3)
# displays help information on the function 'str'
help(str)

#######################################################
######################## Lists ########################
#######################################################

# A list is a container of objects.
# They do not need to be the same
# Mutable

# create a list containing different data types, strings, integers, floats, booleans
values = ['1',2,3.0,False]
# print the length of the list, here it is 4. the list has 4 elements
print len(values)
# print the type of the object, a list! :)
print type(values)
# print the list itself, this will show the content of the list and data structure it is stored in
print values[1]
# just as we could with a string we can access subsections of the list using indexing. Here we print the first 3 entries of the list
print values[:3]
# print from the 3rd (or two-ith element to the last element of the list)
print values[2:]
# create an empty list
l = []
# append a new item to the end of the list, the integer 8
l.append(8)
# append another item to the list, now the list will be l = [8,10], rememeber order is important with lists
l.append(10)
# add another 10 to the end, now l = [8,10,10]
l.append(10)
# same again l = [8,10,10,12]
l.append(12)
# remove the first instance of the integer 10 from the list
l.remove(10)
print l
# remove the zeroeth element from the list
l.remove(l[0])
print l
# create a list of integers from 0 to 10-increment, incremented by 2 using the range function (i.e from 0 to 8)
l = range(0,10,2)
print l
# create a list of integers from -5 to 5-increment, using the default increment = 1
l = range(-5,5)
print l
line = "This is a    \t list -      \t of strings"
# the function split will split a string into substrings using the specified input string as a dividor, it will then store each substring found in a list. Len then counts the length of this list. Here the string is split in 3 since there are two occurences of the '\t' within the string
print len(line.split('\t'))
# as mentioned on last line 
print line.split('\t')
# this is a list comprehension. the statement on the left will be iterated through by the instruction on the right, in this case, the string is just repeated 10 times. The output is a list containing these 10 instances 
print ['add another field' for i in range(10)]
# as above
l = range(-5,5)
print l
# re-order the list from highest to lowest, there is no output from this command as the function acts on the original object
print l.sort(reverse=True)
# as we can see when we print l
print l

#######################################################
######################## Tuples #######################
#######################################################

# Sequence of objects, like lists, but immutable

# create tuple in the same we would create a list but using '(' insteqad of '['
t = (10,40.0,"A")
# print the type ans length of the tuple
print type(t), len(t)
# we cannot change elements of a tuple after is has been created! as illustrated here! This is how they differ from lists
# t[1] = 'B'

#######################################################
################## Dictionaries #######################
#######################################################

# A flexible collection of {key: value} pairs.
# Also called associative arrays or hash maps in other languages.

# create empty dictionary
data = {}
# add 1 boolean element under the key 'k1'
data['k1'] = True
# add 1 integer element under the key 'k2'
data['x2'] = 2
# add 1 float element under the key 100, integers can be used as keys as well as strings! :)
data[100] = 3.0
print data
# length of the dict shows how many objects are stored in it and we can see the data type
print len(data), type(data)
# as above
data['k4'] = 100
# here we compltely overide our original dict with a new one, using this syntax we can put object into the dict as we instantiate it
data = {'number': 10, 1:'string'}
# add another element to the dict, we've put a list inside a dict! This will be useful later in pandas.DataFrames :)
data['c'] = [1,2,3,4]
print data
# print the element stored under the key 1
print data[1]
# here with first access the list from the dict using the key 'c', then we further access the three-ith (4th) element of the list
print data['c'][3]
# print the integer stored under the key numbers
print data['number']

#######################################################
##################### Classes #########################
#######################################################

# Almost everything in python fits into a class
# You can also make classes on your own!

class Car():
	def __init__(self, model='Ford',wheels = 4):

		if wheels < 0 :
			print "A car cannot have less than 0 wheels, so we've made this car have 0 for you"
			wheels = 0	
		
		self.model = model
		self.wheels = wheels
		self.running = False

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