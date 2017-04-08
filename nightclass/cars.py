class Vehicle:
    def __init__(self, make, model, year, color):
        self.model = model
        self.make = make
        self.year = year
        self.color = color
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.make, self.model, self.year, self.color)

    def __repr__(self, spaces):
        self.spaces = spaces
        self.spaces_left = 0






class ParkingLot:
    def __init__(self, spaces):
        self.spaces = spaces
        self.spaces_left = spaces
        self.parked_vehicles = self.create_space_numbers()

    def create_space_numbers(self):
        spaces_diction = {}
        for i in range(self.spaces):
            spaces_diction[i] = None

        return spaces_diction



    def park(self, obj):
        if self.spaces_left > 0:
            self.spaces_left -= 1
            self.parked_vehicles.append(obj)
            print('There are {} spaces left'.format(self.spaces_left))
        else:
            print('There are no spaces left')

    def remove(self):
        car_list = enumerate(self.parked_vehicles)
        for i, v in car_list:
            print('{} is in spot {}'.format(v,i))
        removing = True
        while removing:
            q = input('Which car would you like to remove or (c)ancel?')
            if q.lower == 'cancel' or q.lower() == 'c':
                break
            else:
                try:
                    veh = self.parked_vehicles.pop(int(q))
                    self.spaces_left += 1
                    print('{} has left the parking lot'.format(veh.model))
                    print('There are {} spaces left.'.format(self.spaces_left))
                    removing = False
                except ValueError:
                    print('That is not a valid entry.')
                except IndexError:
                    print('There is no vehicle in that spot.')

plot = ParkingLot(5)

car1 = Vehicle('Dodge', 'Charger', 2017, 'Black')

car2 = Vehicle('Ford', 'Mustang', 2001, 'Red')

car3 = Vehicle('Tesla', "coupe", 2015, 'Green')


diction = {}
diction['key' space number] = 'value'

#key =
plot.park(car1)
plot.park(car2)
plot.park(car3)
plot.remove()





#think about using dictionaries to assign cars to specific spots

#overloading = overwriting the parent class in some way in the children classes
#most builtins can be dundered


"""class Truck(Vehicle):
    def __init__(self, make, model, year, drive):
        Vehicle.__init__(self, make, model, year)
        self.drive = drive

car.drive = '4x4'
car = Vehicle('Jeep', 'Grand Cherokee', 2001)
truck = Truck('Ford', 'F150', 2017 ,'4x4')

print(car.drive)

when building an object, think about what you want to do with the object"""
