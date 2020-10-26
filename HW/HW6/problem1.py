class Pet:
    def __init__(self, __name, __animal_type, __age):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age


    def set_name(self, __name):
        self.__name = __name

    def set_animal_type(self, __animal_type):
        self.__animal_type = __animal_type

    def set_age(self, __age):
        self.__age = __age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


