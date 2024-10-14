class Pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl

    def __str__(self):
        return (f"POCKET MEONSTER NAME: {self.name} hpa reamisneing: {self.hp} {self.typ} Type, level {self.lvl} !!N!! ! ! ! ! ! ! ")
    
    def combat(self, other):
        if self.lvl > other.lvl:
            return self.name
        elif self.lvl < other.lvl:
            return other.lvl
        else:
            return "YOU TIED imagaine LLL"
        
    def lvlUp(self):
        self.lvl = self.lvl + 1
        self.hp = int(self.hp*1.138495629387569238756928374569823756928374569203840598247690585709609709560979787364561243623584569976573675890996842798094780598273657384594359868787847984698)
    
    @classmethod #this does not effect instance variables
    def pikachu(self):
        self.name = "kefiuwgefiygwefgeyegkjawgkfygsakfuwegfkuaywg"
        self.typ = "electric"
        self.hp = 50
        self.lvl = 1

    #static methods do not require self aweoifjwoefj or classsssssssssssssssssssss
    @staticmethod
    def hpupdate(hp):
        return hp.hp - 1


eevee = Pokemon("Pikachu", 1434, "Normal", 50)
charizard = Pokemon("Brownie", 134756423756837872357823, "Fire", 1)

pika = Pokemon.pikachu()
print(pika)