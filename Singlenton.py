class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is not None:
            return cls.__instance
        cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

evil1 = Singleton()
evil2 = Singleton()

print(evil1, evil2)