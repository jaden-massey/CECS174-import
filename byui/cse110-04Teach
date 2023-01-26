import math

class Velo():
    def __init__(self):
        self.mass = 0.0
        self.grav = 0.0
        self.area = 0.0
        self.drag = 0.0
        self.time = 0.0
        self.dens = 0.0
        self.c = 0.0
        self.vel_t = 0.0

    def get(self):
        self.mass = float(input('Mass (in kg): '))
        self.grav = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
        self.time = float(input('Time (in seconds): '))
        self.dens = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
        self.area = float(input('Cross sectional area (in m^2): '))
        self.drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
        self.c = 0.5 * self.dens * self.area * self.drag

    def put(self):
        print(f'\nThe inner value of c is: {self.c:.3f}')
        print(f'The velocity after {self.time} seconds is: {self.vel_t:.3f} m/s')

    def calculate(self):
        self.vel_t = math.sqrt(self.mass * self.grav / self.c) * (1 - math.exp((-math.sqrt(self.mass * self.grav * self.c) / self.mass) * self.time))


print('Welcome to the velocity calculator. Please enter the following:\n')
velocity = Velo()
velocity.get()
velocity.calculate()
velocity.put()




