import PersonClass as pc

def main():
    name = 'Thomas'
    address = '123 main St'
    phone_num = '123-456-7890'
    cust_no = 4455
    MailList = True

    person1 = pc.Person(name, address, phone_num)
    customer1 = pc.Customer(name, address, phone_num, cust_no, MailList)

    person1.print_person()

    print()
    print()
    print()

    customer1.print_person()
main()