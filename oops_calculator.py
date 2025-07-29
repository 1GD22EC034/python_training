class person:
    def print_name(self,name):
        print("My name is"+name)
    def add (self,a,b):
        return a+b
#person creation
person = person()
#calling the method
person.print_name("Shiva")
result = person.add(3,5)
print(result)            