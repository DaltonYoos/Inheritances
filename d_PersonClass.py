
class Person:


    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone

    def print_person(self):

        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Phone Number:', self.__phone)

class Customer(Person):

    def __init__(self, name, address, phone, cus_num, on_list):

        Person.__init__(self, name, address, phone)

        self.__cus_num = cus_num

        self.__on_list = on_list

    def print_person(self):
        print('METHOD #1')
        print('Name:', Person.get_name(self))
        print('Address:', Person.get_address(self))
        print('Phone Number:', Person.get_phone(self))

        print()
        print()

        print('METHOD #2')
        Person.print_person(self)

        print('Customer Number:', self.__cus_num)
        if self.__on_list:
            print('On Mailing List: Yes')
        else:
            print('On Mailing List: No')

    
            