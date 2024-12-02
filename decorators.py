

def cough(func):
    def func_wraper():
        #stuff that happens before function
        print("*clears throat*")
        func()
        #stuff that happens after
        print("*cough*")

    return func_wraper

@cough
def awkward():
    print("Can I get a discount..?")

@cough
def answer():
    print("sir this is a dollar tree")
    
awkward()
answer()