class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def introduce(self):
        print(f"Hello! My name is {self.name} and My breed is {self.breed} and I'm {self.age}old")

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
    
    def woof_woof(self):
        print("Woof Woof")
        
class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 10)

    def arrrr(self):
        print("arrrrr")
        
        
yonu = Puppy(name="younm", breed="dalma")
younyoung = GuardDog(name="youngyoung", breed="bladog")

yonu.introduce()
yonu.woof_woof()
younyoung.introduce()
younyoung.arrrr()