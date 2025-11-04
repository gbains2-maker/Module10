


class Cow(Animal):
    def speak(self):
        print("Moo")
    def display(self):
        print("I am black and white!")
    def move(self):
        print("Slow")
        
class Aardvark(Animal):
    def speak(self):
        print("gobble")
    def display(self):
        print("I am ugly!")
    def move(self):
        print("Fast")
        
class Person(Person):
    def speak(self):
        print("Talk")
    def display(self):
        print("I am Handsome!")
    def move(self):
        print("Moving")
        
animal = Animal()
cow = Cow()
aardvark = Aardvark()
person = Person()
animal_attributes(animal)
animal_attributes(cow)
animal_attributes(aardvark)
animal_attributes(person)