class Purse:
    def __init__(self, valuta, name='Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError('Не верная валюта кошелька')
        self.__money = 0.00
        self.__valuta = valuta
        self.__name = name

    def top_up_balance(self, howmoney):
        self.__money += howmoney
        return  howmoney

    def top_dowm_balance(self, howmoney):
        if self.__money - howmoney < 0:
            print('Не достаточно средств')
            raise ValueError ('Не достаточно средсвт')
        self.__money -= howmoney
        return howmoney

    def Info(self):
        print(self.__name)
        print(self.__valuta)
        print(self.__money)

    def __del__(self):
        print('Кошелек удален.')
        return self.__money


x = Purse('USD')
y = Purse('EUR', 'Bill')

x.top_up_balance(100)
y.top_up_balance(25)

x.top_up_balance(y.top_dowm_balance(8))


x.Info()
print('\n')
y.Info()




