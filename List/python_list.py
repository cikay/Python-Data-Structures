import _ctypes


class MyList:

    def __init__(self) -> None:
        self.__list = [None]*10

    def __setitem__(self, i, value):
        self.__list[i] = id(value)
    
    def __getitem__(self, i):
        return self.__get_by_id(self.__list[i])

    def __get_by_id(self, id):
        return _ctypes.PyObj_FromPtr(id)

my_list = MyList()

my_list[1] = "John"
print(my_list[1])