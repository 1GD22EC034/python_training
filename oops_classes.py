# class person:
#     def print_name(self,name):
#         print("My name is"+name)
#     def sub (self,a,b):
#         return a-b
# #person creation
# person = person()
# #calling the method
# person.print_name("Shiva")
# result = person.sub(8,5)
    # print(result)     
# class City:
#       self.name = name
#         self.country = country

#   def addCityDetails(self,name,country):
# def printCityDetails(self):
#     print("City Nmae:" + self.name)
#     print("Country:" + self.country)
# #object creation
# delhi = City()
# #calling the method
# delhi.addCityDetails("delhi","India")
# delhi.printCityDetails()

# mumbai = City()
# #calling the method
# mumbai.addCityDetails("mumbai","India")
# mumbai.printCityDetails()

from abc import ABC,abstractmethod

class person():
    cityName = "mumbai"
    def printName(self,name):
        print(name)

class Nandini(person):
    def printDetails(Self):
        print("some msg")
obj = Nandini()
obj.cityName = "banglore"
obj.printName("Nandini")            

