#PascalCase use keyword calss.
class Animal:
    #start with constructor.
    def __init__(self, name, species, age, gender, rarity, losses=0):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
        self.losses = losses

    #prints a special way uwu owo :3
    def __str__(self):
        return f"""Name: {self.name}
        
Age: {self.age}
Species: {self.species}
Gender: {self.gender}
Rarity: {self.rarity}"""
    
    #methods are bascislacy functions in the class. so cool right.
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name) < len(other.name):
            self.losses += 1
            return other.name
        else:
            return "YOU TIED imagaine LLL"
    
#store in array teehee usually
cat = Animal("Mr. Beast", "cat", 97, "male", "extinct")
dog = Animal("The Grinch", "dog", 1434, "female", "extinct")

#change values by changing them. so easy
cat.name = "Destroyer of Worlds"

#just call a method by calling it bro its not that deep
print(cat.fight(dog))

print(dog.losses)

cat = None #kil