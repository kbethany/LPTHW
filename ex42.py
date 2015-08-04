#animal is-a object(yes, sort of confusing) look at extra credit
class Animal(object):
    pass

##dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name of some kind
        self.name = name

##cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name of some kind
        self.name = name

##person is-a object
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

##employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## Employee has a salary of some kind
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a Person
mary = Person("Mary")

#mary has-a pet of kind satan
mary.pet = satan

##frank is-a employee and has-a salary of kind 120000
frank = Employee("Frank", 120000)

##frank has-a pet of kind rover
frank.pet = rover

#flipper is-afish
flipper = Fish()

#crouse is-a salmon
crouse = Salmon()

#harry is-a halibut
harry = Halibut()
