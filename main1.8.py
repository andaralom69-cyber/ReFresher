# class Sim:
#     def __init__ (self, name, ):
#         self.name = name

# class Bed:
#     def sleep(self, sim):
#         sim.energy = 100

class Home:
    def __init__(self, name):
        self.name = name

    def sleep(self, sim):
        print(f'{sim.name} is sleeping in {self.name} house')
        sim.energy += 20
        my_sim.hp += 5

    def relax(self, sim):
        sim.energy += 10
        print('Storm Spirit is relaxing: +10 energy')

class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def work(self, sim):
        print(f'{sim.name} is working like {self.title}, he will got 40 dollars')
        sim.money += self.salary
        sim.energy -= 15

class Sim:
    def __init__(self, name, home, job):
        self.name = name
        self.home = home
        self.job = job
        self.energy = 50
        self.money = 100
        self.tango = 1
        self.korm = 0
        self.hp = 50
    def eat(self):
        print(f'{self.name} eat tango')
        self.energy += 10
        self.tango -= 1
        self.hp += 25
        if self.tango == 0:
            print('Storm Spirit has no tango')
    def show_status(self):
        print('-'*30)
        print(f'Name: {self.name}')
        print(f'Energy: {self.energy}')
        print(f'Money: {self.money}')
        print(f'Tangos: {self.tango}')
        print(f'Kormes: {self.korm}')
        print(f'Health: {self.hp}')
        if self.energy <= 0:
            print('Sim is tired')
        if self.money <= 0:
            print('Sim without money')

class Haymer:
    def __init__(self, title2, salary2):
        self.title2 = title2
        self.salary2 = salary2

    def work2(self, sim):
        print(f'{sim.name} is working like {self.title2}, he will got 30 dollars and -5 energy')
        sim.money += self.salary2
        sim.energy -= 5

class macasin:
    def buying(self):
        if my_sim.money > 20:
            my_sim.tango += 1
            my_sim.korm += 1
            print(f'Storm Spirit buy 1 tango and 1 korm')

class pet:
    def korm(self):
        if my_sim.korm > 1:
            my_sim.korm -= 1
            print('Storm Spirit feed his pet')
        else:
            print('Strom Spirir has no korm')

class school:
    def stadying(self):
        my_sim.energy -= 50
        print('Strom Spirit learned new material, and has tired')

# my_bed = Bed()
# my_bed.sleep(my_sim)
my_sim = Sim(name='Storm Spirit', home='tron', job='midder')
my_home = Home(name='Storm Spirit')
my_home.sleep(my_sim)
job = Job(title='gdsher', salary=40)
job.work(my_sim)
my_sim.eat()
my_home.relax(my_sim)
work2 = Haymer(title2='геймер', salary2=30)
work2.work2(my_sim)
macasin = macasin()
macasin.buying()
pet = pet()
pet.korm()
my_sim.show_status()
