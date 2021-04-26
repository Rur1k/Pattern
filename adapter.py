class PrintStr:
    def get(self):
        return 'Привет'

class PrintNumber:
    def get(self):
        return 17

class Adapter(PrintNumber):
    def get(self):
        return str(super(Adapter, self).get())

def PrintData(obj):
    print('Результат: '+obj.get())

DataStr = PrintStr()
#DataInt = PrintNumber()
Data = Adapter()

PrintData(DataStr)
#PrintData(DataInt)
PrintData(Data)

