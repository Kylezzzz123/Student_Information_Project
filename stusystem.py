def main():
    while True:
        menu()
        choice = int(input("Please select your choice: "))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice ==0:
                answer = input("Are you sure to quite? y/n: ")
                if answer == 'y' or answer == 'Y':
                    print("Thanks!")
                    break
                else: 
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def menu():
    print('------------------------------------------Student Information Management System-----------------------')
    print('------------------------------------------------------Function menu--------------------------------------------------------')
    print('\t\t\t\t\t\t1.Input Student information')
    print('\t\t\t\t\t\t2.Search Student information')
    print('\t\t\t\t\t\t3.Delete Student information')
    print('\t\t\t\t\t\t4.Edit Student information')
    print('\t\t\t\t\t\t5.Sort Student information')
    print('\t\t\t\t\t\t6.Calculate Student information')
    print('\t\t\t\t\t\t7.Show Student information')
    print('\t\t\t\t\t\t0.Quit')
    print('---------------------------------------------------------------------------------------------------------------------------')

def insert():
    pass

def search():
    pass

def delete():
    pass

def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass




if __name__ =='__main__':
    main()