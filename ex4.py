cars=100 #sets object cars equal to 100
space_in_a_car = 4.0 #sets object spaceinacar to 4.0 NOTE: all this does is allow the output to have a decimal place later on during operations. otherwise it will just round down. it sounds kind of unwieldy to do this all the time as a practice.
drivers=30
passengers=90
cars_not_driven=cars-drivers #creating new variable carsnotdriven, the value of which is the value of cars less the value of drivers
cars_driven=drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

