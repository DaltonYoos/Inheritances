import d_PersonClass as p

def main():

    name = 'John'
    address = '1234 Main St.'
    phone = '123-456-7890'
    cus_num = '1234'
    on_list_flag = True

    person1 = p.Person(name, address, phone)

    customer1 = p.Customer(name, address, phone, cus_num, on_list_flag)

    person1.print_person()

    print()
    print()
    print()

    customer1.print_person()





main()