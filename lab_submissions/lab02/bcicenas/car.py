class Car():
    #setting an all american default
    def __init__(self, model='Ford', wheels=4):
        self.model = model
        #disallow four wheels
        if wheels <= 0:
            print 'our current universe does not support negative wheels. defaulting to four.'
            wheels = 4
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
