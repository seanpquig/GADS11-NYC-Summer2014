# ### STRINGS
# # This is a comment!
# # Storing a string to the variable s
# s = "Hello world, world"
# # printing the type. It shows 'str' which means it is a string type
# print type(s)
# # printing the number of characters in the string.
# print len(s)
# # Python gave me an error below! I guess we can't change individual parts of a string this way.
# s[0] = 'h'
# # from here continue writing a comment for each line explaining what the following line does.
# s2 = s.replace("world", "python")
# s3 = s2.replace("Hello","monty")
# print s
# print s2
# print s3
# print s[6:11]
# print s[6:]
# print s[-2:]
# s4 = s + ' ' + s3
# print s4
# print s4.find('world')
# print 'A string with value {0} and {1}'.format(10,20.3)
# help(str)


# ### LISTS
# values = ['1',2,3.0,False]
# print len(values)
# print type(values)
# print values
# print values[1]
# print values[:3]
# print values[2:]
# l = []
# l.append(8)
# l.append(10)
# l.append(10)
# l.append(12)
# print l
# l.remove(10)
# print l
# l.remove(l[0])
# print l
# l = range(0,10,2)
# print l
# l = range(-5,5)
# print l
# line = "This is a    \t list -      \t of strings"
# print len(line.split('\t'))
# print line.split('\t')
# print ['add another field' for i in range(10)]
# l = range(-5,5)
# print l
# print l.sort(reverse=True)
# print l


# ### TUPLES
# t = (10,40.0,"A")
# print type(t), len(t)
# t[1] = 'B'


# ### DICTIONARIES
# data = {}
# data['k1'] = True
# data['x2'] = 2
# data[100] = 3.0
# print data
# print len(data), type(data)
# data['k4'] = 100
# data = {'number': 10, 1:'string'}
# data['c'] = [1,2,3,4]
# print data
# print data[1]
# print data['c'][3]
# print data['number']


### CLASSES
import code

class Car():
    def __init__(self, model='Ford', num_wheels=4):
        self.model = model
        if num_wheels <0:
            print 'num wheels must be >=0'
            self.num_wheels = 0
        else:
            self.num_wheels = num_wheels

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

ford = Car(num_wheels=-4)
nissan = Car(model = 'Nissan')
code.interact(local=locals())
ford.running
ford.start()
ford.running
nissan.running
nissan.stop()
