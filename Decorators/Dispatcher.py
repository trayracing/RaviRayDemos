
class Dispatcher:
    def __init__(self):
        self.processors = {}
    
    def Dispatch(self, name):
        self.processors[name]()

    def Add(self, name):
        def AddProcessor(func):
            def Processor():
                print(f'process {name}')
                func()
            self.processors[name] = Processor
            return Processor
        return AddProcessor

dispatcher = Dispatcher()

@dispatcher.Add('Kitchen')
def KitchenColor():
    print('...pink')

@dispatcher.Add('Bedroom')
def BedroomColor():
    print('...blue')

for room in ['Kitchen','Bedroom']:
    dispatcher.Dispatch(room)

#########################################
def OldAdd(self, name, func):
    def Processor():
        print(f'process {name}')
        func()
    self.processors[name] = Processor

Dispatcher.OldAdd = OldAdd

def BathColor():
    print('...green')
dispatcher.OldAdd('Bath', BathColor)

dispatcher.OldAdd('Porch', lambda: print('...yellow'))

for room in ['Bath', 'Porch']:
    dispatcher.Dispatch(room)
