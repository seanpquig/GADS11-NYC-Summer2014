# this describes a car object as was discussed in Lab02

class Car():
    # initialize New object
    def __init__(self, model='Ford', wheels=4):
        self.model = model
        self.running = False
        self.wheels = wheels
        if (wheels < 4) and (wheels > 1):
            print "You are describing a motorcycle"
        elif (wheels < 2) and (wheels > 0):
            print "You are describing a unicycle"
        elif wheels > 4:
            print "You are describing a truck"
        elif wheels <= 0:
            print "You are describing a sled"
            self.wheels = 0
        
    # Alter state of running to True, the car is made to be running.
    def start(self):
        if self.running != True:
            print 'The car started!'
            self.running = True
        else:
            print 'The car is already running!'

    # Alter state of running to False, the car is made no be longer running.
    def stop(self):
        if self.running == True:
            print 'The car stopped!'
            self.running = False
        else:
            print 'The car was not running!'
