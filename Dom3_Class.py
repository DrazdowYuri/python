# Variant 4 - Car

class Car(object):


    def __init__(self, id, brand, model, year, color, price, number):

        self.id = id
        self.color = color
        self.btand = brand
        self.model = model
        self.year = year
        self.price = price
        self.number = number


    def CarAge(self):

        print("Car age is " +str(year))
        return "Braking"

    def ListModels(self):
        if (self.model = "Volvo"):
            print("Volvo car " + self.number)
        else:
            print("Other car " + self.number)




car1 = Car(1,"Volvo","SF1",2010,"blue", 12000,"MI7-4536")
car2 = Car(2,"Ford","Fiesta",2018,"blue", 12000,"MI7-4536")
car3 = Car(3,"Volvo","SF1",2010,"blue", 12000,"MI7-4536")
car4 = Car(4,"Ford","Fiesta",2010,"blue", 12000,"MI7-4536")
car5 = Car(5,"Volvo","SF1",2010,"blue", 12000,"MI7-4536")
car6 = Car(6,"Volvo","SF1",2010,"blue", 12000,"MI7-4536")
car7 = Car(7,"Ford","Scorpio",2000,"blue", 12000,"MI7-4536")
car8 = Car(8,"Ford","Scorpio",2001,"blue", 12000,"MI7-4536")
car9 = Car(9,"Ford","Fiesta",2012,"blue", 12000,"MI7-4536")
car10 = Car(10,"Volvo","SF1",2010,"blue", 12000,"MI7-4536")

print(car1.color)
print(car10.price)



