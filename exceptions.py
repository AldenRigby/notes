#exceptions grahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
#bsaically "if breaks code --> do something else"
#zero division, file not found, value error, type error, index error
#^^ all can be automatically excepted
num = 0
num2 = 0

class NegativeNumberError(Exception):
    pass

while True:
    try:
        num = int(input("tell me a number plssssssssssss: "))
    except ValueError:
        print("that wasnt a whole number you fialure !!!!")
        continue
    else:
        break
while True:
    try:
        num2 = int(input("tell me anoter number plssssssssssss: "))
        if num2 <= 0:
            raise NegativeNumberError
    except ValueError:
        print("that wasnt a whole number you fialure !!!!")
        continue
    except NegativeNumberError as e:
        print("sorry we are negative number racists here. try again")
        print(e)
        continue
    else:
        try:
            print(f"{str(num)} divided by {str(num2)} equals {num/num2}")
        except ZeroDivisionError:
            print("you can't divide by 0 in the real number system. :( try again noob")
            continue
        break
    finally: #runs regardless of if exception was raised or not
        print("whee hee hee")