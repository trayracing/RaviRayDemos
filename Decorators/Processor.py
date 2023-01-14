
#return a function that uses a function
def AddProcessor(func):
    def Processor():
        print('process')
        func()
    return Processor

@AddProcessor
def KitchenColor():
    print('...pink')

KitchenColor()

###################################

def DenColor():
    print('...brown')
DenColor = AddProcessor(DenColor)

DenColor()

##########################

def Pastel(func):
    return 'Light ' + func()

@Pastel
def Hall():
    return 'Fuscia'

print(Hall)