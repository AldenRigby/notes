from functools import reduce

myList = [4,6,8,1.5,5,10,7]
newlist = ["", "wafe", "Awefwaefewa", ""]

#for num in myList:
#    num += 1
#    newlist.append(num)

def increase(num):
    return num+1

def multiple(num):
    if num % 3 == 0:
        return num

print(list(map(increase, myList)))

#print(list(filter(multiple, myList)))

print(list(filter(lambda num: num % 3 == 0, myList)))

print(list(filter(lambda x: x != "", newlist)))

print(list(filter(lambda x: x != "", newlist)))

multiplier = lambda x, y: x*y
print(reduce(multiplier, myList))