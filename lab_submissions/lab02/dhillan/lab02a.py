#Strings
# This is a comment!
# Storing a string to the variable s
s = "Hello world, world"
# printing the type. It shows 'str' which means it is a string type
print type(s)
# printing the number of characters in the string.
print len(s)
# Python gave me an error below! I guess we can't change individual parts of a string this way.
s[0] = 'h'
# from here continue writing a comment for each line explaining what the following line does.
s2 = s.replace("world", "python")
# replaces 'hello' with 'monty'
s3 = s2.replace("Hello","monty")
# print the value of s
print s
# print value of s2
print s2
#print value of s3
print s3
# print the 7th to 10th inclusive element
print s[6:11]
# prints the 7th to end elements
print s[6:]
# prints the second last element
print s[-2:]
# joins string s and s3, separated by a space
s4 = s + ' ' + s3
# prints value of s4
print s4
# returns the position of the string in s4
print s4.find('world')
# inserts values into string
print 'A string with value {0} and {1}'.format(10,20.3)
# help page on strings
help(str)

#Lists
# define a new list with char, int, float, bool
values = ['1',2,3.0,False]
# print the length of the list
print len(values)
# print the type of List
print type(values)
# print list
print values
# print second element of list
print values[1]
# print all values to end
print values[:3]
# print 3rd to last elemebt
print values[2:]
# define new empty list
l = []
# append element
l.append(8)
# append element
l.append(10)
# append element
l.append(10)
# append element
l.append(12)
# print list
print l
# remove first element that is a 10
l.remove(10)
# print list
print l
# remove first element
l.remove(l[0])
# print l
print l
# set l to 0 to 9 (inc) in steps of 2
l = range(0,10,2)
# print l
print l
# set l to range -5 to 4 (inc)
l = range(-5,5)
# print l
print l
# new string with tab character
line = "This is a    \t list -      \t of strings"
# print length of list when splitting line by tab
print len(line.split('\t'))
# print splirt of line by tab character
print line.split('\t')
# print add another field 10 times
print ['add another field' for i in range(10)]
# set l to list of -5 to 4 (inc)
l = range(-5,5)
# print l
print l
# print l sorted in reverse
print l.sort(reverse=True)
# print l
print l

#Tuples
# make new tuple t
t = (10,40.0,"A")
# print t
print type(t), len(t)
# attempt to set second element but can't
t[1] = 'B'

#Dictionaries
# create new data dict
data = {}
# set new key k1 with val True
data['k1'] = True
# set new key x2 with val 2
data['x2'] = 2
# set new key 100 to 3
data[100] = 3.0
# print value data
print data
# print length data, and type
print len(data), type(data)
# set new key k4 with value of 100
data['k4'] = 100
# re-set data with 2 key value pairs in one go
data = {'number': 10, 1:'string'}
# add key c with value list
data['c'] = [1,2,3,4]
# print data
print data
# print data element 2
print data[1]
# print 4th element from key c
print data['c'][3]
# print value from key number
print data['number']

#Classes
# new class Car
class Car():
    # default method for arguments, model is ford and
    # wheels is 4 by default
    def __init__(self, model='Ford', wheels=4):
        # set each of the self variables
        self.model = model
        self.running = False
        #if wheels has been overridden and less than 0
        if wheels < 0:
            # set to 0
            self.wheels = 4
            print 'Can not have negative wheels - set to 4'
        else:
            # else set to user defined wheels
            self.wheels = wheels
    # method to start the car        
    def start(self):
        # if it's not already running, set running True
        if self.running != True:
            print 'The car started!'
            self.running = True
        else:
            print 'The car is already running!'
    # method to stop car running
    def stop(self):
        # if car running, then set to stopped
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
toyota = Car(model = 'Toyota', wheels = -1)
print toyota.wheels