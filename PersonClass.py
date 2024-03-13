#Create a Person Class
class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

    def Show_Info(self):
        print("Name: ", self.__name)
        print("Address: ",self.__address)
        print("Phone Number: ", self.__phone)


class Customer(Person):
    
    def __init_(self,name,address,phone,custNo, MailList):
        Person.__init__(self, name, address, phone, custNo, MailList)

        self.__custNo = custNo
        self.__MailList = MailList
    
    def get_custNo(self):
        return self.__custNo
    def get_MailList(self):
        return self.__MailList
    
def print_person(self):
    print("METHOD 1")
    print("Name: ", self.__name(self))
    print("Address: ",self.__address(self))
    print("Phone Number: ", self.__phone(self))
    print()
    print()
    print("METHOD 2")
    Person.print_person(self)
    print()
    print()
    print("Customer Numer: ",self.__custNo)
    print("On the Mail List: ",self.__MailList)
        
