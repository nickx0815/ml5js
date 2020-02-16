class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class posesData(object):
    __data = ''
    __status = False

    def __init__(self):
        pass

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

@Singleton
class soundData(object):
    __data = ''
    __status = False

    def __init__(self):
        pass

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
