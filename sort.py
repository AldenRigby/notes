from operator import attrgetter
li = (9,1,8,2,7,3,6,4,5)

wheehee = sorted(li)
print(wheehee)

di = {"name": "Tia", "job": "Sales", "age": 28, "os": "Mac"}
hohoho = sorted(di)
print(hohoho)

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)
    
grahhahhah = Employee("Jim Bob", 37, 70000)
grahhahhah2 = Employee("Jamitha", 29, 3)
grahhahhah3 = Employee("greahuewfhawfewaoifej oawiehfawef", 937, .1)

employess = [grahhahhah, grahhahhah2, grahhahhah3]

def wubgbbgubgubg(weee):
    return weee.salary

#these are the same
wabfuwagf = sorted(employess, key=wubgbbgubgubg)
wabfuwagf = sorted(employess, key=attrgetter("salary"))

print(wabfuwagf)