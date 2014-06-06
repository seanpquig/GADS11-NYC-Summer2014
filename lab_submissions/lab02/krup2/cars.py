__author__ = 'krupakar'


class Car():
    # constructor
    def __init__(self, model='Ford', wheels=4):
        self.model = model
        self.running = False
        # Make sure wheels can never be negative
        if wheels < 0:
            print "ERROR: {0} wheels can't be negative".format(self.model)
            self.wheels = 0
        else:
            self.wheels = wheels

    def start(self):
        if not self.running:
            print '{0} started with {1} wheels'.format(self.model, self.wheels)
            self.running = True
        else:
            # don't allow restarting a started car
            print '{0} is already running'.format(self.model)

    def stop(self):
        if self.running:
            print '{0} stopped with {1} wheels'.format(self.model, self.wheels)
            self.running = False
        else:
            # don't allow stopping a stoppe car
            print '{0} is already stopped'.format(self.model)


ford = Car()

nissan = Car(model='Nissan', wheels=-5)

ford.start()

nissan.start()
nissan.stop()


