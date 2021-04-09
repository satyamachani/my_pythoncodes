class vehicle:
    wheels = 4
    def move(self):
        print('Every vehicle move this way')
class car(vehicle):
    def disply(self):
        print('car has',self.wheels,'wheels')
c=car()
c.move()
c.disply()