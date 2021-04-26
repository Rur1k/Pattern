class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

s = Singleton()
print("Созданный object:", s)
s1 = Singleton()
print("Созданный object:", s1)