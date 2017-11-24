class Bike:
    
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print '{} {} {}'.format(self.price, self.max_speed, self.miles)

    def ride(self):
        self.miles += 10
        print "Riding", self.miles 

    def reverse(self):
        self.miles -= 5
        print "Reversing", self.miles

bike_1 = Bike(1000, '60mph')
bike_2 = Bike(500, '50mph')
bike_3 = Bike(200, '40mph')

bike_1.ride()
bike_1.ride()
bike_1.ride()
bike_1.reverse()
bike_1.displayinfo()
bike_2.ride()
bike_2.ride()
bike_2.reverse()
bike_2.reverse()
bike_2.displayinfo()
bike_3.reverse()
bike_3.reverse()
bike_3.reverse()
bike_3.displayinfo()

